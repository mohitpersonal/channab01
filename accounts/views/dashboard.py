
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
			some_day_last_week = timezone.now() - timedelta(days=7)

			print(some_day_last_week, type(some_day_last_week))
			user_obj = User.objects.get(id = int(request.user.id))
			all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, created_on__gt = some_day_last_week).order_by('-created_on')
			all_milking_record_days = []

			for one_record in all_milking_record:
				context = {}

				if one_record.created_on > timezone.now() - timedelta(days=1):
					last_days = timezone.now() - timedelta(days=1)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, created_on__gt = last_days).order_by('-created_on')

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gt = last_days).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = last_days).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)
					context['last_day_morning'] = sum_of_morning
					context['last_day_evening'] = sum_of_evening
					context['created_on'] = one_record.created_on

				if one_record.created_on > timezone.now() - timedelta(days=2):
					last_days = timezone.now() - timedelta(days=2)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, created_on__gt = last_days).order_by('-created_on')

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gt = last_days).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = last_days).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)
					context['last_day_morning'] = sum_of_morning
					context['last_day_evening'] = sum_of_evening
					context['created_on'] = one_record.created_on

				if one_record.created_on > timezone.now() - timedelta(days=3):
					last_days = timezone.now() - timedelta(days=3)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, created_on__gt = last_days).order_by('-created_on')

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gt = last_days).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = last_days).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)
					context['last_day_morning'] = sum_of_morning
					context['last_day_evening'] = sum_of_evening
					context['created_on'] = one_record.created_on


				if one_record.created_on > timezone.now() - timedelta(days=4):
					last_days = timezone.now() - timedelta(days=4)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, created_on__gt = last_days).order_by('-created_on')

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gt = last_days).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = last_days).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)
					context['last_day_morning'] = sum_of_morning
					context['last_day_evening'] = sum_of_evening
					context['created_on'] = one_record.created_on
				if one_record.created_on > timezone.now() - timedelta(days=5):
					last_days = timezone.now() - timedelta(days=5)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, created_on__gt = last_days).order_by('-created_on')

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gt = last_days).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = last_days).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)
					context['last_day_morning'] = sum_of_morning
					context['last_day_evening'] = sum_of_evening
					context['created_on'] = one_record.created_on
				if one_record.created_on > timezone.now() - timedelta(days=6):
					last_days = timezone.now() - timedelta(days=6)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, created_on__gt = last_days).order_by('-created_on')

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gt = last_days).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = last_days).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)
					context['last_day_morning'] = sum_of_morning
					context['last_day_evening'] = sum_of_evening
					context['created_on'] = one_record.created_on
				if one_record.created_on > timezone.now() - timedelta(days=7):
					last_days = timezone.now() - timedelta(days=7)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, created_on__gt = last_days).order_by('-created_on')

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gt = last_days).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = last_days).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)
					context['last_day_morning'] = sum_of_morning
					context['last_day_evening'] = sum_of_evening
					context['created_on'] = one_record.created_on

				all_milking_record_days.append(context)






			print("all_milking_record --------->", all_milking_record_days)

			return render(request, 'livestock/all_milk.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/all_milk.html', locals())
