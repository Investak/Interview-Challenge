from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .forms import ContactForm, SignUpForm
from django.core.mail import send_mail
from .models import *

# Create your views here.
def home(request):
    
    title = 'SignUp for our Newsletter:'
    data = SignUp.objects.all()
    form = SignUpForm(request.POST or None)

    context = {
        'title': title,
        'form':form,
        'data': data
    }

    if form.is_valid():
        instance = form.save(commit = False)
        if not instance.full_name:
            instance.full_name = "Guest"
        instance.save()
        title = "Thank you for signing with us. We will soon get in touch with you."
        context = {
        'title': title,
        }
        

    return render(request,"home.html",context)


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    context = {
        'form':form,
        'title':title,
    }

    if form.is_valid():
    
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        subject = 'Site contact form'
        form_email = settings.EMAIL_HOST_USER
        to_email = [form_email]
        contact_message = "%s: %s via %s" % (form_full_name,form_message,form_email)

        send_mail(subject,contact_message,form_email,to_email,fail_silently=False)
        context = {
        
        'title':"Thank you",
    }

    return render(request,"contact.html",context)


def about(request):
    context = {
    
    }
    return render(request,"about.html",context)

def homescreen(request):
    context = {
        
    }
    return render(request,"homescreen.html",context)

def visualiser(request):
    data_yahoo = Yahoo.objects.all().order_by('-id')
    data_amazon = Amazon.objects.all().order_by('-id')
    data_facebook = Facebook.objects.all().order_by('-id')
    data_twitter = Twitter.objects.all().order_by('-id')
    data_apple = Apple.objects.all().order_by('-id')
    data_priceline = Priceline.objects.all().order_by('-id')
    data_alphabet = Alphabet.objects.all().order_by('-id')
    data_regeneron = Regeneron.objects.all().order_by('-id')
    data_tesla = Tesla.objects.all().order_by('-id')
    data_biogen = Biogen.objects.all().order_by('-id')
    data_baidu = Baidu.objects.all().order_by('-id')
    data_illumina = illumina.objects.all().order_by('-id')
    data_celgene = Celgene.objects.all().order_by('-id')
    data_vodafone = Vodafone.objects.all().order_by('-id')
    data_paypal = Paypal.objects.all().order_by('-id')
    data_texas = Texas.objects.all().order_by('-id')
    data_intel = Intel.objects.all().order_by('-id')
    data_ea = Ea.objects.all().order_by('-id')
    context = {
        'data_yahoo': data_yahoo ,
        'data_amazon': data_amazon,
        'data_facebook': data_facebook,
        'data_twitter': data_twitter,
        'data_apple': data_apple,
        'data_priceline': data_priceline,
        'data_alphabet': data_alphabet,
        'data_regeneron': data_regeneron,
        'data_tesla': data_tesla,
        'data_biogen': data_biogen,
        'data_baidu': data_baidu,
        'data_illumina': data_illumina,
        'data_celgene': data_celgene,
        'data_vodafone': data_vodafone,
        'data_intel': data_intel,
        'data_paypal': data_paypal,
        'data_texas': data_texas,
        'data_ea': data_ea,
    }
    return render(request,"visualiser.html",context)

def companies(request):
    company_list = Company.objects.all()
    paginator = Paginator(company_list, 25)
    page = request.GET.get('page')
    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
            companies = paginator.page(1)
    except EmptyPage:
        companies = paginator.page(paginator.num_pages)
    return render(request, 'companies.html', {'companies': companies})
