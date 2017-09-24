# root URL configuration

from django.conf.urls import url, include
from django.contrib import admin

from home import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^form/$', views.form),
    url(r'^graph/$', views.graph),
]
