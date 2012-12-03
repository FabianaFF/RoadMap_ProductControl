# -- encoding: utf-8 --

from django.db import models

class ProductSpec(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
		
class Product(models.Model):
	product_spec = models.ForeignKey(ProductSpec)
	
	name = models.CharField(max_length=300)
	price = models.FloatField()
	
	def __unicode__(self):
		return self.name
	
class Feature(models.Model):
	product_spec = models.ForeignKey(ProductSpec)
	
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
	
class FeatureValue(models.Model):
	feature = models.ForeignKey(Feature)
	product = models.ForeignKey(Product)
	
	value = models.FloatField()
	
	def __unicode__(self):
		return str(self.value)

	