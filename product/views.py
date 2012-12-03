# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from product.models import Feature, Product

def index(request):    
    product_list = Product.objects.all() #.order_by('-name')[:5]
    return render_to_response('Product/index.html', {'product_list': product_list})    
    
def detail(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    feature_list = Feature.objects.all()
    product_list = Product.objects.all()
    
    return render_to_response('Product/detail.html', {'Product': p, 'feature_list': feature_list,
                                                      'Product_list': product_list,},
                                context_instance=RequestContext(request))
