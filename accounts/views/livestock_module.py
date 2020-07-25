from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from accounts.models import AddedAnimalLiveStock,AllGalleryAddedByUser
from product.models import Category
from django.contrib.auth.models import User



class AddAnimalLivestock(View):

	''' Demonstrate docstring for confirming that this view function will used to add an animal by user'''

	def get(self,request):
		try:
			all_category = Category.objects.values_list('category_name', flat = True)
			return render(request, 'livestock/add_animal.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/add_animal.html', locals())


	def post(self,request):
		try:
			animal_tag = request.POST.get('animal_tag')
			age = request.POST.get('age')
			category = request.POST.get('category')
			animal_bread = request.POST.get('animal_bread')
			gender = request.POST.get('gender')
			male_parent = self.request.POST.get('male_parent')
			female_parent = self.request.POST.getlist('female_parent')
			animal_type = self.request.POST.get('animal_type')
			description = self.request.POST.get('description')
			category_instance = Category.objects.get(category_name = category)

			image = request.FILES.get('main_image')
			user_obj = User.objects.get(id = request.user.id)


			product_obj = AddedAnimalLiveStock.objects.create(animal_tag = animal_tag, date_of_birth=age, animal_breed = animal_bread, category_instance = category_instance, gender = gender,male_parent = male_parent,female_parent = female_parent,  image = image, description = description, animal_type = animal_type,created_by = user_obj)

			ist_image = request.FILES.get('ist_image')
			sec_image = request.FILES.get('sec_image')
			iiird_image = request.FILES.get('iiird_image')
			fourth_image = request.FILES.get('fourth_image')
			fifth_image = request.FILES.get('fifth_image')

			if ist_image:
				AllGalleryAddedByUser.objects.create(product = product_obj,image = ist_image)
			if sec_image:
				AllGalleryAddedByUser.objects.create(product = product_obj,image = sec_image)
			if iiird_image:
				AllGalleryAddedByUser.objects.create(product = product_obj,image = iiird_image)
			if fourth_image:
				AllGalleryAddedByUser.objects.create(product = product_obj,image = fourth_image)
			if fifth_image:
				AllGalleryAddedByUser.objects.create(product = product_obj,image = fifth_image)

			message = 'An animal has been successfully registered for sale purpose.'
			return redirect(reverse('ListingAnimalLiveStock'))
		except Exception as e:
			print(e)
			error = 'Something went wrong, Please try again later'
			return render(request,'product/product_add.html',locals())





class ListingAnimalLiveStock(View):

	''' Demonstrate docstring for confirming that this view function will listing all details of user'''

	def get(self,request):
		try:
			all_animals = AddedAnimalLiveStock.objects.all().order_by('-id')
			return render(request, 'livestock/animal_listing.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_listing.html', locals())










class ViewParticluarAnimal(View):

	''' Demonstrate docstring for confirming that this view function will listing all details of user'''

	def get(self,request):
		try:
			return render(request, 'livestock/animal_info.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())
