from django.shortcuts import render
from django.http import HttpResponse
import json
import io
import csv
import urllib2
from urllib import urlencode
from datetime import date
from .models import *
from django.core.serializers.json import DjangoJSONEncoder

def financialSourceURL(symbol, start_date, end_date):
	params = {
		's': symbol,
		'a': '%02d' % start_date.day,
		'b': '%02d' % start_date.month,
		'c': start_date.year,
		'd': '%02d' % end_date.day,
		'e': '%02d' % end_date.month,
		'f': end_date.year,
		'g': 'd',
		'ignore': '.csv',
	}
	return 'http://real-chart.finance.yahoo.com/table.csv?' + urlencode(params)

def get_historic_data(symbol, start_date, end_date):
	historic_data = (HistoricPrice.objects
	.values_list('date', 'close')
	.filter(date__range=(start_date, end_date), 
		investment__symbol__iexact=symbol))
	if(historic_data.exists()):
		return zip(*historic_data)
	else:
		response = urllib2.urlopen(financialSourceURL(symbol, start_date, end_date))
		csvstring = response.read()
		reader = csv.DictReader(io.StringIO(csvstring.decode('utf-8')), delimiter=',')
		investment = Investment.objects.get(symbol=symbol)
		dates = []
		closing = []
		#prices = []
		for row in reader:
			dates.append(row['Date'])
			closing.append(row['Close'])
			price = HistoricPrice(
				date = row['Date'],
				open = row['Open'],
				high = row['High'],
				low = row['Low'],
				close = row['Close'],
				adjusted_close = row['Adj Close'],
				volume = row['Volume'],
				investment = investment)
			price.save()
		#HistoricPrice.bulk_create(prices)
		return (dates, closing)

def generate_graph(symbol="YHOO", 
	start_date=date(2016,1,1), 
	end_date=date(2016,2,3)):
	(dates, closing) = get_historic_data(symbol, start_date, end_date)
	return [{
		'x': dates,
		'y': closing,
		'type': 'scatter'
	}]

def index(request):
	context = {
	'data': json.dumps(generate_graph(), cls=DjangoJSONEncoder)
	}
	return render(request, 'portfolios/index.html', context);

from django.utils.dateparse import parse_date
def get_prices(start_date, end_date):
  prices = HistoricPrice.objects

  if start_date is None:
    start_date = prices.earliest('date').date
  else:
    start_date = parse_date(start_date)

  if end_date is None:
    end_date = prices.latest('date').date
  else:
    end_date = parse_date(end_date)

  if end_date > date.today():
    raise Exception("Cannot be in future")
  if start_date > end_date:
    raise Exception("Start must be less than end")
 
  if prices_available_locally(start_date, end_date):
    return get_prices_locally(start_date, end_date)
  else:
    return get_prices_remotely(start_date, end_date)

def prices_available_locally(start_date, end_date):
  from datetime import date
  prices = HistoricPrice.objects

  if prices.earliest('date').date > start_date:
    return False
  elif prices.latest('date').date < end_date:
    return False
  else:
    return HistoricPrice.objects.filter(date__range=(start_date, end_date)).exists()

def get_prices_remotely(start_date, end_date):
  pass
  
def get_prices_locally(start_date, end_date):
  import csv
  prices = HistoricPrice.objects
  if start_date and end_date:
    prices = prices.filter(date__range=(start_date, end_date))
  elif start_date:
    prices = prices.filter(date__gte=start_date)
  elif end_date:
    prices = prices.filter(date__lte=end_date)
  else:
    prices = prices.all()
  return prices

def generate_csv(prices, fields, labels):
  dates = prices.values_list('date', flat=True)
  vals = ['%.2f;%.2f;%.2f'%t for t in prices.values_list(*fields)]

  response = HttpResponse(content_type='text/csv')
  writer = csv.writer(response)
  writer.writerow(labels)
  writer.writerows(zip(dates, vals))
  return response

def info(request):
  start_date = request.GET.get('start')
  end_date = request.GET.get('end')
  prices = get_prices(start_date, end_date)
  fields = ['low', 'close', 'high']
  labels = ['date', 'YHOO']
  return generate_csv(prices, fields, labels)

def needs_remote(request):
  from django.http import JsonResponse
  start_date = request.GET.get('start')
  end_date = request.GET.get('end')
  if start_date is not None:
    start_date = parse_date(start_date)
  if end_date is not None:
    end_date = parse_date(end_date)

  data = {
    'locally': prices_available_locally(start_date, end_date),
    'earliest': str(HistoricPrice.objects.earliest('date').date),
    'latest': str(HistoricPrice.objects.latest('date').date),
  }
  return JsonResponse(data)

from django.views.generic.base import TemplateView

class StockCompareView(TemplateView):
  
  template_name = "portfolios/compare.html"
  
  def get_context_data(self, **kwargs):
    context = super(StockCompareView, self).get_context_data(**kwargs)
    context['symbols'] = Investment.objects.values_list('symbol', flat=True)
    return context