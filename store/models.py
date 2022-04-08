from django.db import models
from category.models import Category
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=128)
	slug = models.SlugField(max_length=64)
	description = models.TextField(max_length=512, blank=True, null=True)
	price = models.FloatField()
	images = models.ImageField(upload_to='photos/products')
	stock = models.IntegerField()
	is_available = models.BooleanField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def get_url(self):
		return reverse('product_detail', args=[self.category.slug, self.slug])

	def __str__(self):
		return self.product_name


