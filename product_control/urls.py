from django.conf.urls import patterns, include, url
from api.handlers import ProductHandler,ProducSpectHandler
from piston.resource import Resource

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
    #url(r'product/(?P<product_id>\d*)/$', products_resource), 
)
