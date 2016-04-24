import datetime
import json
from pprint import pprint

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.utils import timezone

from yahoo_finance import Share

from .models import *
from .forms import *


def companies(request):
    company_list = Company.objects.all()
    paginator = Paginator(company_list, 50)
    page = request.GET.get('page')
    try:
        all_companies = paginator.page(page)
    except PageNotAnInteger:
        all_companies = paginator.page(1)
    except EmptyPage:
        all_companies = paginator.page(paginator.num_pages)
    return render(request, 'portfolio/company_list.html', {'all_companies': all_companies,})


# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return redirect('/accounts/profile/')
    else:
        form = ContactForm()

        if request.method == 'POST':
            form = ContactForm(data=request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']

                auto_sub = 'Automatic reply from Akj'
                auto_msg = """Thank You.\nWe will get to get back to you as soon as possible"""

                send_mail(subject, message, email,
                          ['yourid@example.com'], fail_silently=False)
                send_mail(auto_sub, auto_msg, settings.EMAIL_HOST_USER,
                          [email], fail_silently=False)
                return redirect('/thankyou/')

        return render(request, 'portfolio/index.html', {
            'form': form,
        })


def profile(request):
    portfolios = Portfolio.objects.filter(user__username=request.user)
    c = {'portfolios': portfolios}
    return render(request, 'portfolio/profile.html', c)

def portfolio_details(request, name):
    users_portfolio = get_object_or_404(Portfolio, name=name)
    # for company in users_portfolio.companies.all():
    #     print(company)
    c = {'users_portfolio': users_portfolio}
    return render(request, 'portfolio/portfolio_details.html', c)

def add_portfolio(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            for company in form.cleaned_data['companies']:
                portfolio.companies.add(company)
            return redirect('/accounts/profile/')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/add_portfolio.html',
                  {'form': form})


def thankyou(request):
    return render(request, 'portfolio/thankyou.html')


def plotgraph(request, name, duration):
    if duration == '1Month':
        start = datetime.date.today() - datetime.timedelta(1*365/12)
    elif duration == '3Month':
        start = datetime.date.today() - datetime.timedelta(3*365/12)
    elif duration == '6Month':
        start = datetime.date.today() - datetime.timedelta(6*365/12)
    else:
        start = datetime.date.today() - datetime.timedelta(365)

    end = datetime.date.today()

    sharedata = [['Date', name]]

    c_share = Share(name).get_historical(str(start), str(end))

    for data in c_share:
        sharedata.append([data['Date'],data['Open']])


    # pprint(sharedata)
    return HttpResponse(json.dumps(sharedata), content_type='application/json')


def edit_portfolio(request, name):
    portfolio = get_object_or_404(Portfolio, name=name)
    if request.method == "POST":
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            for company in form.cleaned_data['companies']:
                portfolio.companies.add(company)
            return redirect('/')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio/edit_portfolio.html',
                  {'form': form, 'pname': name})
