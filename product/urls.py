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
    # Examples:
    # url(r'^$', 'product_control.views.home', name='home'),
    # url(r'^product_control/', include('product_control.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$', views.index, name='index'),
    #url(r'^product/$', 'product.views.index'),
    url(r'^product/$', products_resource),
    url(r'^$/', products_resource),
    url(r'^product/(?P<product_id>\d+)/$', products_resource),
    url(r'^product_spec/$', products_spec_resource),
    url(r'^product_spec/(?P<product_spec_id>\d+)/$', products_spec_resource),
    #url(r'^product/(?P<product_id>\d+)/featurevalues/$', ),
    #url(r'^product/(?P<product_id>\d+)/vote/$', 'product.views.vote'),
)
