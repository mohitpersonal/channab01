
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
import string,random
from accounts.models import UserProfileInfo












class DashBoardView(View):

	''' Demonstrate docstring for confirming that this view function will register a user'''

	def get(self,request):

		try:
			return render(request, 'livestock/dashboard.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/dashboard.html', locals())









class AllMilkRecord(View):

	''' Demonstrate docstring for confirming that this view function will register a user'''

	def get(self,request):

		try:
			return render(request, 'livestock/all_milk.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/all_milk.html', locals())
