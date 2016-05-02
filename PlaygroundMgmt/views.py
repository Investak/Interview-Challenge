import json
import logging
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import requires_csrf_token
from yahoo_finance import Share
from models import *

def index(request):
  return HttpResponse("quick check...")

#---------------------------------------------------------------- PORTFOLIO SPECIFIC REQUESTS

@login_required(login_url='/PlaygroundMgmt/ajax_kicked')
def portfolio_list(request):
  """
    request portfolio list of a particular user
  """
  response = {'portfolios': []}

  # read the current user
  cuser = request.user;

  portfolio = Portfolio.objects.filter(user__username = cuser)
  for p in portfolio: # format response to send to client 
    serial_ins = []
    for ins in p.instruments.all():
      serial_ins.append({'name': ins.name, 'id': ins.id, 'ticker': ins.ticker});
    response['portfolios'].append({'name': p.name, 'id': p.id, 'instruments': serial_ins})

  return JsonResponse(response)

@login_required(login_url='/PlaygroundMgmt/ajax_kicked')
def portfolio_create(request):
  """
    create a new portfolio for the logged user
  """
  newName = request.POST['name']
  p = Portfolio(name = newName, user = request.user)
  p.save()

  response = {'name': p.name, 'id': p.id, 'instruments': []}
  return JsonResponse(response)

@login_required(login_url='/PlaygroundMgmt/ajax_kicked')
def portfolio_edit(request):
  p = Portfolio.objects.get(pk = request.POST['portfolio_id'])
  p.name = request.POST['portfolio_name']
  p.save()

  return redirect('/portfolio_list')

@login_required(login_url='/PlaygroundMgmt/ajax_kicked')
def portfolio_delete(request):
  """
    delete the requested portfolio
  """
  portfolio = Portfolio.objects.get(pk = request.POST['portfolio_id'])
  portfolio.delete()

  return redirect('/portfolio_list')

@login_required(login_url='/PlaygroundMgmt/ajax_kicked')
def portfolio_add_ins(request):
  """
    add an instrument to an existing portfolio
  """
  portfolio = Portfolio.objects.get(id = request.POST['portfolio_id']);
  instrument = Instrument.objects.get(id = request.POST['instrument_id']);
  # size is not being processed right now,
  size =  0.1
  # TODO: define how the weights will work

  try:
    inv = Investment.objects.get(portfolio__id = request.POST['portfolio_id'], 
      instrument__id = request.POST['instrument_id'])
  except Investment.DoesNotExist:
    investment = Investment(portfolio = portfolio, instrument = instrument, size = size)
    investment.save()

  return redirect('./portfolio_list')

@login_required(login_url='/PlaygroundMgmt/ajax_kicked')
def portfolio_del_ins(request):
  """
    delete an instrument from a portfolio
  """
  inv = Investment.objects.get(portfolio__id = request.POST['portfolio_id'], 
    instrument__id = request.POST['instrument_id'])
  inv.delete()

  return redirect('./portfolio_list') 

def portfolio_performance(request):
  """ return the performance history of a portfolio
      to be drawn in the line chart
  """
  response = {}

  # TODO handle error connection to API

  share = Share(request.GET['ticker'])
  #TODO dynamic dates
  start = '2015-01-01';
  end = '2016-04-01';
  response['history'] = share.get_historical(start, end)

  return JsonResponse(json.dumps(response), safe = False)

#---------------------------------------------------------------- INSTRUMENT SPECIFIC REQUESTS

@login_required(login_url='/PlaygroundMgmt/ajax_kicked')
def instruments_list(request):
  """
    get the list of instrument for search
    TODO: progressive loading
  """
  response = {'instruments': []}
  _ins = Instrument.objects.all()[:30]; # for testing
  for ins in _ins:
    response['instruments'].append({
      'id': ins.id, 'name': ins.name, 'market': ins.market.name,
      'asset_type': ins.asset_type.name
    })

  return HttpResponse(json.dumps(response), content_type = 'application/json')    

def instrument_history(request, ticker, start, end):
  """ return history data of a particular instrument using
      using Yahoo Finance API 
      https://pypi.python.org/pypi/yahoo-finance
  """
  response = {}
  response['ticker'] = ticker
  response['start'] = start
  response['end'] = end

  # call yahoo-finance
  share = Share(ticker)
  response['history'] = share.get_historical(start, end)

  return HttpResponse(json.dumps(response), content_type = 'application/json')

#---------------------------------------------------------------- USERS HANDLERS

@requires_csrf_token
def loguser(request):
  """
    a simple django based authentication...
  """
  if request.method == 'GET': # send login view
    return render(request, 'PlaygroundMgmt/login.html')

  username = request.POST['username']
  password = request.POST['password']

  user = authenticate(username = username, password = password)
  if user is not None:
    if user.is_active:
      login(request, user)
      
      return redirect('/static/index.html')
    else:
      # TODO: Return a 'disabled account' error message
      context = RequestContext(request)
      context['authenticated_msg'] = 'not_active'
      
      return render(request, 'PlaygroundMgmt/login.html', context_instance=context)
  else:
    # TODO: send login view with error msg
    context = RequestContext(request)
    context['authenticated_msg'] = 'no_user'
    
    return render(request, 'PlaygroundMgmt/login.html', context_instance=context)

def ajax_kicked(request):
  response = 'unauthorized'
  return HttpResponse(json.dumps(response), content_type = 'application/json')