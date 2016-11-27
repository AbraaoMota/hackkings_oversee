from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^home$', views.home, name='home'),
  url(r'^dashboard$', views.dashboard, name='dashboard'),
  url(r'^new_channel$', views.new_channel, name='new_channel'),
]
