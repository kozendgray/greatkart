from django.db import models
from django.urls import reverse

class Category(models.Model):
	category_name = models.CharField(max_length=64)
	slug = models.SlugField(max_length=64, unique=True)
	description = models.TextField(max_length=512)
	category_image = models.ImageField(upload_to='photos/categories')

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):
		return reverse('products_by_category', args = [self.slug])

	def __str__(self):
		return self.category_name