"""zunjiasite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from stock_apply import views as stock_apply_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^input/', stock_apply_views.stock_input,name='input'),
    url(r'^list/', stock_apply_views.showlist,name='list'),
    url(r'^contact/', stock_apply_views.contact,name='contact'),
    url(r'^info_submit/', stock_apply_views.info_submit,name='info_submit'),
    url(r'^sync/', stock_apply_views.show_sync,name='sync'),
]
