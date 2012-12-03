from product.models import *
from django.contrib import admin

admin.site.register(ProductSpec)
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(FeatureValue)

class ProductInline(admin.TabularInline):
	model = Product
	extra = 1
	
class ProductSpecAdmin(admin.ModelAdmin):
	inlines = [ProductInline]