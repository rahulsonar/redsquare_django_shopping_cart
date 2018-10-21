import datetime

from django.db import models
from django.utils import timezone


class Product(models.Model):
	product_title = models.CharField(max_length=200)
	product_description = models.CharField(max_length=300)
	product_price = models.FloatField()
	product_status = models.IntegerField()
	date_added = models.DateTimeField('date created')

	def __str__(self):
		return self.product_title