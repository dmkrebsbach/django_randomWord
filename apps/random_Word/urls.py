from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^createWord$', views.createWord),
    url('^reset$', views.reset),
]