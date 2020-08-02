
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
			user_obj = User.objects.get(id = int(request.user.id))
			all_milking_record_days = []

			last_days = timezone.now().date()- timedelta(days=1)

			all_animal_saved = AddedAnimalLiveStock.objects.filter(is_active = True, created_by = user_obj).order_by('-id')
			day_wise_milk_list = []
			total_morning_column = 0
			total_eveining_sum = 0
			all_sum_total = 0

			for one_animal in all_animal_saved:
				one_dict = {}

				all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,animal_instance = one_animal).values_list('morning_time', flat = True)

				all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,animal_instance = one_animal).values_list('evening_time', flat = True)

				all_milking_record_morning = list(map(int, all_milking_record_morning))
				all_milking_record_evening = list(map(int, all_milking_record_evening))


				sum_of_morning = sum(all_milking_record_morning)
				total_morning_column =sum_of_morning + total_morning_column 

				sum_of_evening = sum(all_milking_record_evening)
				total_eveining_sum = sum_of_evening + total_eveining_sum

				total_sum_of_one_row = sum_of_morning + sum_of_evening
				all_sum_total = total_sum_of_one_row + all_sum_total


				one_dict['sum_of_morning'] = sum_of_morning
				one_dict['sum_of_evening'] = sum_of_evening
				one_dict['sum_of_both'] = total_sum_of_one_row
				one_dict['animal_tag'] = one_animal.animal_tag
				day_wise_milk_list.append(one_dict)







			some_day_last_week = timezone.now().date() - timedelta(days=7)
			monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
			monday_of_this_week = monday_of_last_week + timedelta(days=7)
			seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=monday_of_last_week, created_on__lt=monday_of_this_week).values_list('morning_time', flat = True)
			last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=monday_of_last_week, created_on__lt=monday_of_this_week).values_list('evening_time', flat = True)			
			seven_record_morning = list(map(int, seven_record_morning))
			last_week_evening = list(map(int, last_week_evening))
			seven_record_morning = sum(seven_record_morning)
			last_week_evening = sum(last_week_evening)
			sec_last_days_create = monday_of_last_week.strftime("%d" + "%B")
			range_to = monday_of_this_week.strftime("%d"+"%B")
			range_created_on = sec_last_days_create + ' ' + '-' + ' ' + range_to
			sum_of_ist_week =  last_week_evening + seven_record_morning





			one_some_day_last_week = timezone.now().date() - timedelta(days=14)
			one_monday_of_last_week = one_some_day_last_week - timedelta(days=(one_some_day_last_week.isocalendar()[2] - 1))
			one_monday_of_this_week = one_monday_of_last_week + timedelta(days=7)
			one_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=one_monday_of_last_week, created_on__lt=one_monday_of_this_week).values_list('morning_time', flat = True)
			one_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=one_monday_of_last_week, created_on__lt=one_monday_of_this_week).values_list('evening_time', flat = True)			
			one_seven_record_morning = list(map(int, one_seven_record_morning))
			one_last_week_evening = list(map(int, one_last_week_evening))
			one_seven_record_morning = sum(one_seven_record_morning)
			one_last_week_evening = sum(one_last_week_evening)
			one_sec_last_days_create = one_monday_of_last_week.strftime("%d" + "%B")
			one_range_to = one_monday_of_this_week.strftime("%d"+"%B")
			one_range_created_on = one_sec_last_days_create + ' ' + '-' + ' ' + one_range_to
			one_sum_of_ist_week =  one_last_week_evening + one_seven_record_morning


			two_some_day_last_week = timezone.now().date() - timedelta(days=21)
			two_monday_of_last_week = two_some_day_last_week - timedelta(days=(two_some_day_last_week.isocalendar()[2] - 1))
			two_monday_of_this_week = two_monday_of_last_week + timedelta(days=7)
			two_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=two_monday_of_last_week, created_on__lt=two_monday_of_this_week).values_list('morning_time', flat = True)
			two_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=two_monday_of_last_week, created_on__lt=two_monday_of_this_week).values_list('evening_time', flat = True)			
			two_seven_record_morning = list(map(int, two_seven_record_morning))
			two_last_week_evening = list(map(int, two_last_week_evening))
			two_seven_record_morning = sum(two_seven_record_morning)
			two_last_week_evening = sum(two_last_week_evening)
			two_sec_last_days_create = two_monday_of_last_week.strftime("%d" + "%B")
			two_range_to = two_monday_of_this_week.strftime("%d"+"%B")
			two_range_created_on = two_sec_last_days_create + ' ' + '-' + ' ' + two_range_to
			two_sum_of_ist_week =  two_last_week_evening + two_seven_record_morning


			three_some_day_last_week = timezone.now().date() - timedelta(days=28)
			three_monday_of_last_week = three_some_day_last_week - timedelta(days=(three_some_day_last_week.isocalendar()[2] - 1))
			three_monday_of_this_week = three_monday_of_last_week + timedelta(days=7)
			three_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=three_monday_of_last_week, created_on__lt=three_monday_of_this_week).values_list('morning_time', flat = True)
			three_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=three_monday_of_last_week, created_on__lt=three_monday_of_this_week).values_list('evening_time', flat = True)			
			three_seven_record_morning = list(map(int, three_seven_record_morning))
			three_last_week_evening = list(map(int, three_last_week_evening))
			three_seven_record_morning = sum(three_seven_record_morning)
			three_last_week_evening = sum(three_last_week_evening)
			three_sec_last_days_create = three_monday_of_last_week.strftime("%d" + "%B")
			three_range_to = three_monday_of_this_week.strftime("%d"+"%B")
			three_range_created_on = three_sec_last_days_create + ' ' + '-' + ' ' + three_range_to
			three_sum_of_ist_week =  three_last_week_evening + three_seven_record_morning


			fourth_some_day_last_week = timezone.now().date() - timedelta(days=35)
			fourth_monday_of_last_week = fourth_some_day_last_week - timedelta(days=(fourth_some_day_last_week.isocalendar()[2] - 1))
			fourth_monday_of_this_week = fourth_monday_of_last_week + timedelta(days=7)
			fourth_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=fourth_monday_of_last_week, created_on__lt=fourth_monday_of_this_week).values_list('morning_time', flat = True)
			fourth_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=fourth_monday_of_last_week, created_on__lt=fourth_monday_of_this_week).values_list('evening_time', flat = True)			
			fourth_seven_record_morning = list(map(int, fourth_seven_record_morning))
			fourth_last_week_evening = list(map(int, fourth_last_week_evening))
			fourth_seven_record_morning = sum(fourth_seven_record_morning)
			fourth_last_week_evening = sum(fourth_last_week_evening)
			fourth_sec_last_days_create = fourth_monday_of_last_week.strftime("%d" + "%B")
			fourth_range_to = fourth_monday_of_this_week.strftime("%d"+"%B")
			fourth_range_created_on = fourth_sec_last_days_create + ' ' + '-' + ' ' + fourth_range_to
			fourth_sum_of_ist_week =  fourth_last_week_evening + fourth_seven_record_morning


			fifth_some_day_last_week = timezone.now().date() - timedelta(days=42)
			fifth_monday_of_last_week = fifth_some_day_last_week - timedelta(days=(fifth_some_day_last_week.isocalendar()[2] - 1))
			fifth_monday_of_this_week = fifth_monday_of_last_week + timedelta(days=7)
			fifth_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=fifth_monday_of_last_week, created_on__lt=fifth_monday_of_this_week).values_list('morning_time', flat = True)
			fifth_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=fifth_monday_of_last_week, created_on__lt=fifth_monday_of_this_week).values_list('evening_time', flat = True)			
			fifth_seven_record_morning = list(map(int, fifth_seven_record_morning))
			fifth_last_week_evening = list(map(int, fifth_last_week_evening))
			fifth_seven_record_morning = sum(fifth_seven_record_morning)
			fifth_last_week_evening = sum(fifth_last_week_evening)
			fifth_sec_last_days_create = fifth_monday_of_last_week.strftime("%d" + "%B")
			fifth_range_to = fifth_monday_of_this_week.strftime("%d"+"%B")
			fifth_range_created_on = fifth_sec_last_days_create + ' ' + '-' + ' ' + fifth_range_to
			fifth_sum_of_ist_week =  fifth_last_week_evening + fifth_seven_record_morning


			sixth_some_day_last_week = timezone.now().date() - timedelta(days=49)
			sixth_monday_of_last_week = sixth_some_day_last_week - timedelta(days=(sixth_some_day_last_week.isocalendar()[2] - 1))
			sixth_monday_of_this_week = sixth_monday_of_last_week + timedelta(days=7)
			sixth_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=sixth_monday_of_last_week, created_on__lt=sixth_monday_of_this_week).values_list('morning_time', flat = True)
			sixth_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=sixth_monday_of_last_week, created_on__lt=sixth_monday_of_this_week).values_list('evening_time', flat = True)			
			sixth_seven_record_morning = list(map(int, sixth_seven_record_morning))
			sixth_last_week_evening = list(map(int, sixth_last_week_evening))
			sixth_seven_record_morning = sum(sixth_seven_record_morning)
			sixth_last_week_evening = sum(sixth_last_week_evening)
			sixth_sec_last_days_create = sixth_monday_of_last_week.strftime("%d" + "%B")
			sixth_range_to = sixth_monday_of_this_week.strftime("%d"+"%B")
			sixth_range_created_on = sixth_sec_last_days_create + ' ' + '-' + ' ' + sixth_range_to
			sixth_sum_of_ist_week =  sixth_last_week_evening + sixth_seven_record_morning






















			###########  monthly

			one_month_some_day_last_week = timezone.now().date()

			get_last_month = one_month_some_day_last_week.month - 1
			print(get_last_month)
			import calendar
			range_of_date = calendar.monthrange(one_month_some_day_last_week.year, get_last_month)
			print(range_of_date)




			one_month_monday_of_last_week = one_month_some_day_last_week - timedelta(days=(one_month_some_day_last_week.isocalendar()[2] - 3))

			one_month_monday_of_this_week = one_month_monday_of_last_week + timedelta(days=21)
			one_month_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=one_month_monday_of_last_week, created_on__lt=one_month_monday_of_this_week).values_list('morning_time', flat = True)
			one_month_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=one_month_monday_of_last_week, created_on__lt=one_month_monday_of_this_week).values_list('evening_time', flat = True)			
			one_month_seven_record_morning = list(map(int, one_month_seven_record_morning))
			one_month_last_week_evening = list(map(int, one_month_last_week_evening))
			one_month_seven_record_morning = sum(one_month_seven_record_morning)
			one_month_last_week_evening = sum(one_month_last_week_evening)
			one_month_sec_last_days_create = one_month_monday_of_last_week.strftime("%d" + "%B")
			one_month_range_to = one_month_monday_of_this_week.strftime("%d"+"%B")
			one_month_range_created_on = one_month_sec_last_days_create + ' ' + '-' + ' ' + one_month_range_to
			one_month_sum_of_ist_week =  one_month_last_week_evening + one_month_seven_record_morning





			second_month_some_day_last_week = timezone.now().date() - timedelta(days=60)
			second_month_monday_of_last_week = second_month_some_day_last_week - timedelta(days=(second_month_some_day_last_week.isocalendar()[2] - 3))
			print("\n" * 3)
			print("second_month_monday_of_last_week------------------------->", second_month_monday_of_last_week)

			second_month_monday_of_this_week = second_month_monday_of_last_week + timedelta(days=21)
			second_month_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=second_month_monday_of_last_week, created_on__lt=second_month_monday_of_this_week).values_list('morning_time', flat = True)
			second_month_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=second_month_monday_of_last_week, created_on__lt=second_month_monday_of_this_week).values_list('evening_time', flat = True)			
			second_month_seven_record_morning = list(map(int, second_month_seven_record_morning))
			second_month_last_week_evening = list(map(int, second_month_last_week_evening))
			second_month_seven_record_morning = sum(second_month_seven_record_morning)
			second_month_last_week_evening = sum(second_month_last_week_evening)
			second_month_sec_last_days_create = second_month_monday_of_last_week.strftime("%d" + "%B")
			second_month_range_to = second_month_monday_of_this_week.strftime("%d"+"%B")
			second_month_range_created_on = second_month_sec_last_days_create + ' ' + '-' + ' ' + second_month_range_to
			second_month_sum_of_ist_week =  second_month_last_week_evening + second_month_seven_record_morning


			mont_third_some_day_last_week = timezone.now().date() - timedelta(days=28)
			mont_third_monday_of_last_week = mont_third_some_day_last_week - timedelta(days=(mont_third_some_day_last_week.isocalendar()[2] - 1))
			mont_third_monday_of_this_week = mont_third_monday_of_last_week + timedelta(days=28)
			mont_third_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=mont_third_monday_of_last_week, created_on__lt=mont_third_monday_of_this_week).values_list('morning_time', flat = True)
			mont_third_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=mont_third_monday_of_last_week, created_on__lt=mont_third_monday_of_this_week).values_list('evening_time', flat = True)			
			mont_third_seven_record_morning = list(map(int, mont_third_seven_record_morning))
			mont_third_last_week_evening = list(map(int, mont_third_last_week_evening))
			mont_third_seven_record_morning = sum(mont_third_seven_record_morning)
			mont_third_last_week_evening = sum(mont_third_last_week_evening)
			mont_third_sec_last_days_create = mont_third_monday_of_last_week.strftime("%d" + "%B")
			mont_third_range_to = mont_third_monday_of_this_week.strftime("%d"+"%B")
			mont_third_range_created_on = mont_third_sec_last_days_create + ' ' + '-' + ' ' + mont_third_range_to
			mont_third_sum_of_ist_week =  mont_third_last_week_evening + mont_third_seven_record_morning


			month_forth_some_day_last_week = timezone.now().date() - timedelta(days=35)
			month_forth_monday_of_last_week = month_forth_some_day_last_week - timedelta(days=(month_forth_some_day_last_week.isocalendar()[2] - 1))
			month_forth_monday_of_this_week = month_forth_monday_of_last_week + timedelta(days=35)
			month_forth_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=month_forth_monday_of_last_week, created_on__lt=month_forth_monday_of_this_week).values_list('morning_time', flat = True)
			month_forth_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=month_forth_monday_of_last_week, created_on__lt=month_forth_monday_of_this_week).values_list('evening_time', flat = True)			
			month_forth_seven_record_morning = list(map(int, month_forth_seven_record_morning))
			month_forth_last_week_evening = list(map(int, month_forth_last_week_evening))
			month_forth_seven_record_morning = sum(month_forth_seven_record_morning)
			month_forth_last_week_evening = sum(month_forth_last_week_evening)
			month_forth_sec_last_days_create = month_forth_monday_of_last_week.strftime("%d" + "%B")
			month_forth_range_to = month_forth_monday_of_this_week.strftime("%d"+"%B")
			month_forth_range_created_on = month_forth_sec_last_days_create + ' ' + '-' + ' ' + month_forth_range_to
			month_forth_sum_of_ist_week =  month_forth_last_week_evening + month_forth_seven_record_morning


			month_fifth_some_day_last_week = timezone.now().date() - timedelta(days=42)
			month_fifth_monday_of_last_week = month_fifth_some_day_last_week - timedelta(days=(month_fifth_some_day_last_week.isocalendar()[2] - 1))
			month_fifth_monday_of_this_week = month_fifth_monday_of_last_week + timedelta(days=42)
			month_fifth_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=month_fifth_monday_of_last_week, created_on__lt=month_fifth_monday_of_this_week).values_list('morning_time', flat = True)
			month_fifth_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=month_fifth_monday_of_last_week, created_on__lt=month_fifth_monday_of_this_week).values_list('evening_time', flat = True)			
			month_fifth_seven_record_morning = list(map(int, month_fifth_seven_record_morning))
			month_fifth_last_week_evening = list(map(int, month_fifth_last_week_evening))
			month_fifth_seven_record_morning = sum(month_fifth_seven_record_morning)
			month_fifth_last_week_evening = sum(month_fifth_last_week_evening)
			month_fifth_sec_last_days_create = month_fifth_monday_of_last_week.strftime("%d" + "%B")
			month_fifth_range_to = month_fifth_monday_of_this_week.strftime("%d"+"%B")
			month_fifth_range_created_on = month_fifth_sec_last_days_create + ' ' + '-' + ' ' + month_fifth_range_to
			month_fifth_sum_of_ist_week =  month_fifth_last_week_evening + month_fifth_seven_record_morning


			mont_sixth_some_day_last_week = timezone.now().date() - timedelta(days=49)
			mont_sixth_monday_of_last_week = mont_sixth_some_day_last_week - timedelta(days=(mont_sixth_some_day_last_week.isocalendar()[2] - 1))
			mont_sixth_monday_of_this_week = mont_sixth_monday_of_last_week + timedelta(days=49)
			mont_sixth_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=mont_sixth_monday_of_last_week, created_on__lt=mont_sixth_monday_of_this_week).values_list('morning_time', flat = True)
			mont_sixth_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=mont_sixth_monday_of_last_week, created_on__lt=mont_sixth_monday_of_this_week).values_list('evening_time', flat = True)			
			mont_sixth_seven_record_morning = list(map(int, mont_sixth_seven_record_morning))
			mont_sixth_last_week_evening = list(map(int, mont_sixth_last_week_evening))
			mont_sixth_seven_record_morning = sum(mont_sixth_seven_record_morning)
			mont_sixth_last_week_evening = sum(mont_sixth_last_week_evening)
			mont_sixth_sec_last_days_create = mont_sixth_monday_of_last_week.strftime("%d" + "%B")
			mont_sixth_range_to = mont_sixth_monday_of_this_week.strftime("%d"+"%B")
			mont_sixth_range_created_on = mont_sixth_sec_last_days_create + ' ' + '-' + ' ' + mont_sixth_range_to
			mont_sixth_sum_of_ist_week =  mont_sixth_last_week_evening + mont_sixth_seven_record_morning

			seven_month_some_day_last_week = timezone.now().date() - timedelta(days=49)
			seven_month_monday_of_last_week = seven_month_some_day_last_week - timedelta(days=(seven_month_some_day_last_week.isocalendar()[2] - 1))
			seven_month_monday_of_this_week = seven_month_monday_of_last_week + timedelta(days=49)
			seven_month_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=seven_month_monday_of_last_week, created_on__lt=seven_month_monday_of_this_week).values_list('morning_time', flat = True)
			seven_month_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=seven_month_monday_of_last_week, created_on__lt=seven_month_monday_of_this_week).values_list('evening_time', flat = True)			
			seven_month_seven_record_morning = list(map(int, seven_month_seven_record_morning))
			seven_month_last_week_evening = list(map(int, seven_month_last_week_evening))
			seven_month_seven_record_morning = sum(seven_month_seven_record_morning)
			seven_month_last_week_evening = sum(seven_month_last_week_evening)
			seven_month_sec_last_days_create = seven_month_monday_of_last_week.strftime("%d" + "%B")
			seven_month_range_to = seven_month_monday_of_this_week.strftime("%d"+"%B")
			seven_month_range_created_on = seven_month_sec_last_days_create + ' ' + '-' + ' ' + seven_month_range_to
			seven_month_sum_of_ist_week =  seven_month_last_week_evening + seven_month_seven_record_morning










			last_year_some_day_last_week = timezone.now().date() - timedelta(days=49)
			last_year_monday_of_last_week = last_year_some_day_last_week - timedelta(days=(last_year_some_day_last_week.isocalendar()[2] - 1))
			last_year_monday_of_this_week = last_year_monday_of_last_week + timedelta(days=49)
			last_year_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=last_year_monday_of_last_week, created_on__lt=last_year_monday_of_this_week).values_list('morning_time', flat = True)
			last_year_last_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=last_year_monday_of_last_week, created_on__lt=last_year_monday_of_this_week).values_list('evening_time', flat = True)			
			last_year_seven_record_morning = list(map(int, last_year_seven_record_morning))
			last_year_last_week_evening = list(map(int, last_year_last_week_evening))
			last_year_seven_record_morning = sum(last_year_seven_record_morning)
			last_year_last_week_evening = sum(last_year_last_week_evening)
			last_year_sec_last_days_create = last_year_monday_of_last_week.strftime("%d" + "%B")
			last_year_range_to = last_year_monday_of_this_week.strftime("%d"+"%B")
			last_year_range_created_on = last_year_sec_last_days_create + ' ' + '-' + ' ' + last_year_range_to
			last_year_sum_of_ist_week =  last_year_last_week_evening + last_year_seven_record_morning

			second_year_some_day_second_week = timezone.now().date() - timedelta(days=49)
			second_year_monday_of_second_week = second_year_some_day_second_week - timedelta(days=(second_year_some_day_second_week.isocalendar()[2] - 1))
			second_year_monday_of_this_week = second_year_monday_of_second_week + timedelta(days=49)
			second_year_seven_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=second_year_monday_of_second_week, created_on__lt=second_year_monday_of_this_week).values_list('morning_time', flat = True)
			second_year_second_week_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte=second_year_monday_of_second_week, created_on__lt=second_year_monday_of_this_week).values_list('evening_time', flat = True)			
			second_year_seven_record_morning = list(map(int, second_year_seven_record_morning))
			second_year_second_week_evening = list(map(int, second_year_second_week_evening))
			second_year_seven_record_morning = sum(second_year_seven_record_morning)
			second_year_second_week_evening = sum(second_year_second_week_evening)
			second_year_sec_second_days_create = second_year_monday_of_second_week.strftime("%d" + "%B")
			second_year_range_to = second_year_monday_of_this_week.strftime("%d"+"%B")
			second_year_range_created_on = second_year_sec_second_days_create + ' ' + '-' + ' ' + second_year_range_to
			second_year_sum_of_ist_week =  second_year_second_week_evening + second_year_seven_record_morning














			return render(request, 'livestock/all_milk.html', locals())

		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/all_milk.html', locals())
