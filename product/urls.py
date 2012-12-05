from django.conf.urls import patterns, include, url
from product import views
from api.handlers import ProductHandler,ProducSpectHandler
from piston.resource import Resource
from django.views.generic.simple import direct_to_template
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
#    url(r'^lista/$', direct_to_template, {'template': 'product_ext/products.html'}),
)
