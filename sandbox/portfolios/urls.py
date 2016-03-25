from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
	url(r'^info/', info, name='info'),
	url(r'^needs_remote/', needs_remote),
	url(r'^compare/', StockCompareView.as_view(), name='chart'),
	url(r'^$', index, name='index'),
]
