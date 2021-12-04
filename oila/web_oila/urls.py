from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('report', views.report),
]
