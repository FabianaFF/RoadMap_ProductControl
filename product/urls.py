from django.conf.urls import patterns, include, url
from product import views
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
    url(r'^$', views.index, name='index'),
    #url(r'^product/$', 'product.views.index'),
    #url(r'^product/(?P<product_id>\d+)/$', 'product.views.detail'),
    url(r'^(?P<product_id>\d+)/$', 'product.views.detail'),
   # url(r'^product/(?P<product_id>\d+)/results/$', 'product.views.results'),
    #url(r'^product/(?P<product_id>\d+)/vote/$', 'product.views.vote'),
)
