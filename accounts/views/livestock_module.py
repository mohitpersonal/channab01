from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

class AddAnimalLivestock(View):

	''' Demonstrate docstring for confirming that this view function will used to add an animal by user'''

	def get(self,request):
		try:
			return render(request, 'livestock/add_animal.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/add_animal.html', locals())





class ListingAnimalLiveStock(View):

	''' Demonstrate docstring for confirming that this view function will listing all details of user'''

	def get(self,request):
		try:
			return render(request, 'livestock/animal_listing.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_listing.html', locals())
