
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
import string,random


from accounts.models import AddedAnimalLiveStock,AllGalleryAddedByUser,HeathInformation,MilKLitre,DescriptionTable,ParentsChild


from datetime import timedelta
from django.utils import timezone





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
			context = {}
			user_obj = User.objects.get(id = int(request.user.id))
			all_milking_record_days = []

			last_days = timezone.now().date()- timedelta(days=1)


			all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = last_days).values_list('morning_time', flat = True)

			all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = last_days).values_list('evening_time', flat = True)

			all_milking_record_morning = list(map(int, all_milking_record_morning))
			all_milking_record_evening = list(map(int, all_milking_record_evening))


			sum_of_morning_ist = sum(all_milking_record_morning)
			sum_of_evening_ist = sum(all_milking_record_evening)
			last_days_first = last_days
			sum_of_both_ist  = sum_of_morning_ist + sum_of_evening_ist





			sec_last_days = timezone.now().date()- timedelta(days=2)

			sec_last_days_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = sec_last_days).values_list('morning_time', flat = True)

			sec_last_days_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = sec_last_days).values_list('evening_time', flat = True)

			sec_last_days_morning = list(map(int, sec_last_days_morning))
			sec_last_days_evening = list(map(int, sec_last_days_evening))


			two_last_day_morning = sum(sec_last_days_morning)
			two_last_day_evening = sum(sec_last_days_evening)
			sec_last_days_create = sec_last_days
			sum_of_both_Secon =  sum(sec_last_days_morning) +  sum(sec_last_days_evening)


#### 3rd
			three_created_on = timezone.now().date()- timedelta(days=3)

			all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = three_created_on).values_list('morning_time', flat = True)

			all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = three_created_on).values_list('evening_time', flat = True)

			three_last_day_morning = list(map(int, all_milking_record_morning))
			three_last_day_evening = list(map(int, all_milking_record_evening))

			three_last_day_morning = sum(three_last_day_morning)
			three_last_day_evening = sum(three_last_day_evening)
			sum_of_three = three_last_day_evening + three_last_day_morning



### 4th
			fourth_created = timezone.now().date()- timedelta(days=4)
			fourth_created_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = fourth_created).values_list('morning_time', flat = True)

			fourth_created_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = fourth_created).values_list('evening_time', flat = True)

			make_list_morning = list(map(int, fourth_created_morning))
			make_list__evening = list(map(int, fourth_created_evening))


			fourth_sum_of_morning = sum(make_list_morning)
			fourth_sum_of_evening = sum(make_list_morning)
			sum_of_forth = fourth_sum_of_morning + fourth_sum_of_evening


### 5th

			fifth_created = timezone.now().date()- timedelta(days=5)
			fifth_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = fifth_created).values_list('morning_time', flat = True)

			fifth_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = fifth_created).values_list('evening_time', flat = True)

			fifth_milking_record_morning = list(map(int, fifth_milking_record_morning))
			fifth_milking_record_evening = list(map(int, fifth_milking_record_evening))


			fifth_milking_record_morning = sum(fifth_milking_record_morning)
			fifth_milking_record_evening = sum(fifth_milking_record_evening)
			sum_of_fifth = fifth_milking_record_morning + fifth_milking_record_evening



###
			sixth_create = timezone.now().date()- timedelta(days=6)
			sixth_create_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = sixth_create).values_list('morning_time', flat = True)

			sixth_create_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = sixth_create).values_list('evening_time', flat = True)

			sixth_create_record_morning = list(map(int, sixth_create_record_morning))
			sixth_create_record_evening = list(map(int, sixth_create_record_evening))


			sixth_create_record_morning = sum(sixth_create_record_morning)
			sixth_create_record_evening = sum(sixth_create_record_evening)

			sum_of_sixth = sixth_create_record_morning + sixth_create_record_evening

#### last
			seven = timezone.now().date()- timedelta(days=7)
			seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = seven).values_list('morning_time', flat = True)

			seven_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on = seven).values_list('evening_time', flat = True)

			seven_record_morning = list(map(int, seven_record_morning))
			seven_record_evening = list(map(int, seven_record_evening))


			seven_record_morning = sum(seven_record_morning)
			seven_record_evening = sum(seven_record_evening)
			sum_of_seventh = seven_record_morning + seven_record_evening


			all_morning_column = seven_record_morning + sixth_create_record_morning + fifth_milking_record_morning + fourth_sum_of_morning + three_last_day_morning + two_last_day_morning + sum_of_morning_ist

			all_colum_evening = seven_record_evening + sixth_create_record_evening + fifth_milking_record_evening + fourth_sum_of_evening + three_last_day_evening + two_last_day_evening + sum_of_evening_ist

			total_colum_evening = sum_of_seventh + sum_of_sixth + sum_of_fifth + sum_of_forth + sum_of_three + sum_of_both_Secon + sum_of_both_ist





			return render(request, 'livestock/all_milk.html', locals())

		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/all_milk.html', locals())
