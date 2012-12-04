from django.conf.urls import patterns, include, url
from product import views
from api.handlers import ProductHandler,ProducSpectHandler
from piston.resource import Resource
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

products_resource = Resource(handler = ProductHandler)
products_spec_resource = Resource(handler = ProducSpectHandler)

urlpatterns = patterns('',
    url(r'^$', products_resource),    
    url(r'^(?P<product_id>\d+)/$', products_resource),
    url(r'^product_spec/$', products_spec_resource),
    url(r'^product_spec/(?P<product_spec_id>\d+)/$', products_spec_resource),
)
