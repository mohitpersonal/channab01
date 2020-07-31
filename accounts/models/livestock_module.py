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
	date_of_birth = models.DateField(auto_now_add = True)
	animal_breed = models.CharField(max_length = 100, null = True, blank = True)
	category_instance = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	cost_of_animal = models.FloatField(null = True, blank = True)
	date_of_purchase =  models.DateField(auto_now_add = True)

	gender = models.CharField(max_length=1000,choices = choices, null = True, blank = True)
	male_parent = models.IntegerField(null = True, blank = True)
	female_parent = models.IntegerField(null = True, blank = True)
	animal_type = models.CharField(max_length = 15, null = True, blank = True)
	description = models.TextField(null = True, blank = True)

	image = models.ImageField(upload_to='livestock_main_img/', blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on  = models.DateTimeField(auto_now = True)
	created_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_add')
	updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_updated_by')
	is_admin_verified = models.BooleanField(default = False)
	is_call_verified = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)

	def __str__(self):
		return self.animal_tag





class AllGalleryAddedByUser(models.Model):

	'''DEMONSTRATE docstring for confirming that this view based function will give store all those images added by particular user for particular product'''


	product = models.ForeignKey(AddedAnimalLiveStock, on_delete=models.CASCADE, null = True, blank = True)
	image = models.ImageField(upload_to='gallery_livestock/', blank=True, null=True)

	def __str__(self):
		return self.product.animal_tag






class HeathInformation(models.Model):

	'''Demonstrate docstring for confirming that this class based will store the heath related infor in database'''

	animal_instance = models.ForeignKey(AddedAnimalLiveStock, on_delete = models.CASCADE, null = True, blank = True)
	is_active = models.BooleanField(default = True)
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on  = models.DateTimeField(auto_now = True)
	created_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_heath_created')
	updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_heath_updated')
	cost_amount = models.IntegerField()
	tag_name = models.CharField(max_length = 100)
	text_description = models.TextField(null = True, blank = True)






class MilKLitre(models.Model):

	'''Demonstrate docstring for confirming that this class based will store the heath related infor in database'''

	animal_instance = models.ForeignKey(AddedAnimalLiveStock, on_delete = models.CASCADE, null = True, blank = True)
	is_active = models.BooleanField(default = True)
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on  = models.DateTimeField(auto_now = True)
	created_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_milk_created')
	updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_milk_updated')
	morning_time = models.CharField(max_length = 100)
	evening_time = models.CharField(max_length = 100)





class DescriptionTable(models.Model):

	'''Demonstrate docstring for confirming that this class based will store the heath related infor in database'''

	animal_instance = models.ForeignKey(AddedAnimalLiveStock, on_delete = models.CASCADE, null = True, blank = True)
	is_active = models.BooleanField(default = True)
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on  = models.DateTimeField(auto_now = True)
	created_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_description_created')
	updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'animal_description_updated')
	description = models.TextField()







class ParentsChild(models.Model):

	animal_instance = models.ForeignKey(AddedAnimalLiveStock, on_delete = models.CASCADE, null = True, blank = True)
	child_id = models.IntegerField(null = True, blank = True)
	is_active = models.BooleanField(default = True)
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on  = models.DateTimeField(auto_now = True)
	created_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'child_created')
	updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'child_updated')
