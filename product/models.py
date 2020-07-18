from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class MarketAddByAdmin(models.Model):

	''' Demonstrate doctstring for confirming that this table will store all markets adding by an superadmin
	'''

	market_name = models.CharField(max_length = 25, null = True, blank = True)
	market_image = models.FileField(null = True, blank = True)
	date = models.DateTimeField(auto_now_add = True)
	description  = models.TextField(null = True, blank = True)

	is_active = models.BooleanField(default = True)
	location = models.CharField(max_length = 40, null = True, blank = True)

class Product(models.Model):

	'''Demonstrate docstring for confirming that this class will store all product added by user'''

	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	mobilenumber = models.CharField(max_length=100)
	category_instance = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	image = models.ImageField(upload_to='main_img/', blank=True, null=True)
	created = models.DateTimeField(default=timezone.now)
	city = models.CharField(max_length=200, blank=True, null=True)
	slug = models.SlugField(blank=True, null=True)
	animal_type = models.CharField(max_length = 15, null = True, blank = True)
	age_of_animal = models.CharField(max_length = 10, null = True, blank = True)

	is_admin_verified = models.BooleanField(default = False)
	is_call_verified = models.BooleanField(default = False)


	def save(self, *args, **kwargs):
		if not self.slug and self.name:
			self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class ProductImage(models.Model):

	'''Demonstrate docstring for confirming that this class will store all images of product'''

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products/', blank=True, null=True)
	def __str__(self):
		return self.product.name


class Category(models.Model):

	'''Demonstrate docstring for confirming that this class will store all categories of product'''

	category_name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='categories/', blank=True, null=True)
	description = models.TextField()


	slug = models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug and self.category_name:
			self.slug = slugify(self.category_name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.category_name

	def get_absolute_url(self):
		return reverse('product_list_category', args=[self.slug])



class ProductMarket(models.Model):

	''' Demonstrate docstring for confirming this table is used for all markets of current product'''

	market_instance = models.ForeignKey(MarketAddByAdmin, on_delete = models.CASCADE, null = True, blank = True)
	product_instance = models.ForeignKey(Product, on_delete = models.CASCADE, null = True, blank = True)




class CommentReviewsStar(models.Model):

	''' Demonstrate docstring for confirming this table is used for saved comment and reviews on particular product'''

	comment_on_post = models.CharField(max_length = 500, null = True, blank = True)
	product_instance = models.ForeignKey(Product, on_delete = models.CASCADE, null = True, blank = True)
	stars_counting = models.IntegerField(null = True, blank = True)
	created_on = models.DateTimeField(auto_now_add = True)
	mobile_number = models.CharField(max_length = 25, null = True, blank = True)
	name = models.CharField(max_length = 25, null = True, blank = True)
	



class PriceFilter(models.Model):

	min_val = models.CharField(max_length = 10,null = True, blank = True)
	max_val = models.CharField(max_length = 10,null = True, blank = True)
	is_active = models.BooleanField(default = True)

















