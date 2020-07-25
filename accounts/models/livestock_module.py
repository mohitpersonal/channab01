from django.db import models
from product.models import Category
from django.contrib.auth.models import User





class AddedAnimalLiveStock(models.Model):

	'''Demonstrate docstring for confirming that this class will store all product added by logged in user'''

	choices=(
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
	animal_tag = models.CharField(max_length=200)
	date_of_birth = models.DateTimeField(auto_now_add = True)
	animal_breed = models.CharField(max_length = 100, null = True, blank = True)
	category_instance = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

	gender = models.CharField(max_length=1000,choices = choices, null = True, blank = True)
	male_parent = models.CharField(max_length=100,null = True, blank = True)
	female_parent = models.CharField(max_length=100,null = True, blank = True)
	animal_type = models.CharField(max_length = 15, null = True, blank = True)
	description = models.TextField(null = True, blank = True)

	image = models.ImageField(upload_to='main_img/', blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on  = models.DateTimeField(auto_now = True)
	created_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_add')
	updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_updated_by')
	is_admin_verified = models.BooleanField(default = False)
	is_call_verified = models.BooleanField(default = False)

	def __str__(self):
		return self.animal_tag



class AllGalleryAddedByUser(models.Model):

	'''DEMONSTRATE docstring for confirming that this view based function will give store all those images added by particular user for particular product'''


	product = models.ForeignKey(AddedAnimalLiveStock, on_delete=models.CASCADE, null = True, blank = True)
	image = models.ImageField(upload_to='products/', blank=True, null=True)

	def __str__(self):
		return self.product.animal_tag










