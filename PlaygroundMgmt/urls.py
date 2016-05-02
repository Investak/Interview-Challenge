from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^loguser$', views.loguser, name = 'loguser'),
	url(r'^ajax_kicked$', views.ajax_kicked, name = 'ajax_kicked'),
	url(r'^portfolio_create$', views.portfolio_create, name = 'portfolio_create'),
	url(r'^portfolio_list$', views.portfolio_list, name = 'portfolio_list'),
	url(r'^portfolio_edit$', views.portfolio_edit, name = 'portfolio_edit'),
	url(r'^portfolio_delete$', views.portfolio_delete, name = 'portfolio_delete'),
	url(r'^portfolio_add_ins$', views.portfolio_add_ins, name = 'portfolio_add_ins'),
	url(r'^portfolio_del_ins$', views.portfolio_del_ins, name = 'portfolio_del_ins'),
	url(r'^portfolio_performance$', views.portfolio_performance, name = 'portfolio_performance'),
	url(r'^instrument_history/(?P<ticker>.*)/(?P<start>.*)/(?P<end>.*)$', 
		views.instrument_history, name = 'instrument_history'),
	url(r'^instruments_list$', views.instruments_list, name = 'instruments_list'),
	url(r'^$', views.loguser, name = 'loguser')
]