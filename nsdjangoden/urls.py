from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/?$', views.home, name='home'),
    url(r'/about', views.about, name='about'),
    url(r'^firstladyswap/?$', views.index, name='flindex'),
    url(r'^firstladyswap/(?P<pres_id>[0-9]+)/detail/?$', views.detail, name='fldetail'),
    url(r'^firstladyswap/(?P<pres_id>[0-9]+)/?$', views.detail, name='fldetail'),
    url(r'^firstladyswap/(?P<pres_id>[0-9]+)/voting/?$', views.voting, name='flvoting'),
    url(r'^firstladyswap/(?P<pres_id>[0-9]+)/vote/?$', views.vote, name='flvotear'),
    url(r'^firstladyswap/(?P<pres_id>[0-9]+)/voting/vote/?$', views.vote, name='flvote'),
    url(r'^firstladyswap/results/?$', views.all_results, name='flallresults'),
    url(r'^firstladyswap/results/(?P<pres_id>[0-9]+)/?$', views.results, name='flresults'),
]