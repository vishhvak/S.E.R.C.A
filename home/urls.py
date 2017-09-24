from django.conf.urls import url, include
from django.contrib import admin

from home import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'form/', views.form),
]
