from django.conf.urls import patterns, include, url
from api.handlers import ProductHandler,ProducSpectHandler
from piston.resource import Resource
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'product_control.views.home', name='home'),
    # url(r'^product_control/', include('product_control.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/', include('product.urls')),
    #url(r'^product/', products_resource),
    #url(r'^product_spec/', products_spec_resource),
    (r'^api/', include('api.urls')),
    url(r'^lista/$', direct_to_template, {'template': 'product_ext/product_list.html'}),
    url(r'^lista2/$', direct_to_template, {'template': 'product_spec_ext/product_spec_list.html'}),
    url(r'^lista2/detail/(?P<id>\d+)/$', direct_to_template, {'template': 'product_spec_ext/product_spec_detail.html'}),    
    url(r'^lista2/(?P<product_id>\d+)/$', direct_to_template, {'template': 'product_ext/product_list.html'}),
    
    #(r'^product/lista', direct_to_template, {''}),
    #url(r'product/(?P<product_id>\d*)/$', products_resource), 
)
