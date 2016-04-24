from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(regex=r'^companies/$', view=companies, name='companies'),
    url(r'^accounts/profile/$', profile, name='profile'),
    url(r'^portfolio/add/$', add_portfolio, name='add_portfolio'),
    url(r'^portfolio/(?P<name>[-\w\d ]+)$', portfolio_details, name='portfolio_details'),
    url(regex=r'^portfolio/edit/(?P<name>[-\w\d ]+)$', view=edit_portfolio, name='edit_portfolio'),
    url(regex=r'^graph/(?P<name>[-\w\d ]+)/(?P<duration>[-\w\d ]+)', view=plotgraph, name='plotgraph'),
    url(r'^thankyou/', thankyou, name='thankyou'),
]
