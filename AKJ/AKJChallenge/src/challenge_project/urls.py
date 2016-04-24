"""challenge_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [

	url(r'^$','visualiser.views.home',name='home'),
    
	url(r'^contact/$','visualiser.views.contact',name='contact'),
	url(r'^about/$','visualiser.views.about',name='about'),

    url(r'^homescreen/$','visualiser.views.homescreen',name='homescreen'),
    url(r'^companies/$','visualiser.views.companies',name='companies'),
    url(r'^visualiser/$','visualiser.views.visualiser',name='visualiser'),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
