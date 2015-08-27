"""controllerweb URL Configuration

   url pattern - 
   runplaybook/<playbook-name>/<ipaddress>/

   Executed ansbile playbook on the ip provided
"""
from django.conf.urls import include, url
from django.contrib import admin
from controllerweb.views import runplaybook


urlpatterns = [
    url(r'^runplaybook/(\w+)/(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/$', runplaybook),
]
