from piston.handler import BaseHandler
from piston.utils import rc, require_mime, require_extended
from product.models import Product, ProductSpec, Feature, FeatureValue
from rest_framework import exceptions
from django.http import HttpResponse
from aifc import Error

#Post: create, delete: delete, put: update
class ProductHandler(BaseHandler):
    allowed_methods = ('GET','POST','PUT','DELETE')
    model = Product   
    fields = ('id', 'name', 'price', ('features', ('value',)))
    
    
    @classmethod
    def resource_uri(cls, product):
        return ('product', [ 'json', ])
    
    def read(self, request, product_id=None):
        if product_id:
            prod = Product.objects.get(id=product_id)
            feature_values = FeatureValue.objects.filter(product_id=prod.id)
            prod.features = feature_values
            return prod
        else:
            prods = Product.objects.all()
            
            for p in prods:
                feature_values = FeatureValue.objects.filter(product_id=p.id)
                p.features = feature_values
                  
            return prods
            
    def create(self, request):
        
        attrs = self.flatten_dict(request.POST)

        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            prod = Product(name=attrs['name'], value=attrs['price']) 
            prod.product_spec = ProductSpec.objects.filter(product_spec_id=attrs['product_spec_id'])
            prod.save()
            
            return prod

    def delete(self,prod_id):
        prod = Product.objects.get(pk=prod_id)
        
        if prod:
            prod.delete()
            return rc.DELETED
        else:
            return Product.DoesNotExist
            
    def update(self, request):
        attrs = self.flatten_dict(request.PUT)

        prod = Product.objects.filter(id=attrs['id'])
        
        if prod:
            prod.name = attrs['name']
            prod.price = attrs['price'] 
            prod.product_spec = ProductSpec.objects.filter(product_spec_id=attrs['product_spec_id'])            
            prod.save()            
            return prod
        else:
            return Product.DoesNotExist
        
class ProducSpectHandler(BaseHandler):
    allowed_methods = ('GET','POST','PUT','DELETE')
    model = ProductSpec   
    fields = ('id', 'name', ('features', ('name', 'description', )))
    
    
    @classmethod
    def resource_uri(cls, ProductSpec):
        return ('ProductSpec', [ 'json', ])
    
    def read(self, request, product_spec_id=None):
        if product_spec_id:
            prod_spec = ProductSpec.objects.get(id=product_spec_id)
            prod_spec.features = Feature.objects.get(product_spec_id=prod_spec.id)
            return prod_spec
        else:
            prod_specs = ProductSpec.objects.all()
            
            for p in prod_specs:
                p.features = Feature.objects.get(product_spec_id=p.id)
                
            return prod_specs
        
    def create(self, request, *args, **kwargs):
        """
        request.POST['ProductSpec'] = ProductSpec
        try:
            result = super(ProducSpectHandler, self).create(
                   request, *args, **kwargs)
            return result
        except:
            return HttpResponse(status=415)
        """ 
        attrs = self.flatten_dict(request.POST)
       
        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            prod_spec = Product(name=attrs['name'])
            prod_spec.save()
            
            return prod_spec
            

    def delete(self,prod_spec_id):
        prod_spec = ProductSpec.objects.get(pk=prod_spec_id)
        
        if prod_spec:
            prod_spec.delete()
            return rc.DELETED
        #else:
            #raise exceptions.APIException(Exception.message="No data found to delete")
            #exit(0)
            
    def update(self, request):
        attrs = self.flatten_dict(request.PUT)

        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            prod_spec = ProductSpec.objects.filter(attrs['id'])
            prod_spec.name = attrs['name']
            prod_spec.save()
            
            return prod_spec

class FeatureValueHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = FeatureValue   
    fields = ('value')
    
    @classmethod
    def resource_uri(cls, FeatureValue):
        return ('FeatureValue', [ 'json', ])
    
    def read(self, request, id=None):
        if id:
            return FeatureValue.objects.get(id=id)
        else:
            return FeatureValue.DoesNotExist
