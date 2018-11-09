import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
	category_name = models.CharField(max_length=200)
	parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True, null=True, limit_choices_to={'parent' : None})

	def __str__(self):
		return self.category_name

class Product(models.Model):
	product_title = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	product_description = models.TextField()
	product_price = models.FloatField()
	product_status = models.IntegerField()
	quantity = models.IntegerField()
	product_image = models.FileField(upload_to='products/static/uploads',max_length=200)
	date_added = models.DateTimeField('date created')

	def __str__(self):
		return self.product_title

class ProductAttribute(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	meta_name = models.CharField(max_length=30)
	meta_value = models.CharField(max_length=300)

	def __str__(self):
		return self.meta_name

