from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from accounts.models import AddedAnimalLiveStock,AllGalleryAddedByUser,HeathInformation,MilKLitre,DescriptionTable,ParentsChild
from product.models import Category
from django.contrib.auth.models import User

from django.http import HttpResponse
import json,sys

from datetime import timedelta
from django.utils import timezone


class AddAnimalLivestock(View):

	''' Demonstrate docstring for confirming that this view function will used to add an animal by user'''

	def get(self,request):
		try:

			all_category = Category.objects.values_list('category_name', flat = True)
			male_parent = AddedAnimalLiveStock.objects.filter(gender = 'Male').values('animal_tag', 'id')
			female_parent = AddedAnimalLiveStock.objects.filter(gender = 'Female').values('animal_tag','id')

			return render(request, 'livestock/add_animal.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/add_animal.html', locals())


	def post(self,request):
		try:
			animal_tag = request.POST.get('animal_tag')
			age = request.POST.get('age')
			import dateparser
			age = dateparser.parse(age)


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


			product_obj = AddedAnimalLiveStock.objects.create(animal_tag = animal_tag, animal_breed = animal_bread, category_instance = category_instance, gender = gender,male_parent = male_parent,female_parent = female_parent,  image = image, description = description, animal_type = animal_type,created_by = user_obj)
			product_obj.date_of_birth = age
			product_obj.save()

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
			requested_user = User.objects.get(id = request.user.id)
			all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user).order_by('-id')
			all_animal_list = []
			for animal_detail in all_animals:
				animal_list_dict = {}
				age_str = animal_detail.date_of_birth
				day = age_str.day
				month = age_str.month
				year = age_str.year
				born = date(year, month, day)
				today = date.today()
				year_result = 0
				month_result = 0
				try:
					birthday = born.replace(year = today.year)
				except ValueError:
					birthday = born.replace(year = today.year, month = born.month + 1, day = 1) 
				if birthday > today:
					year_result = today.year - born.year - 1
				else:
					if today.year == born.year:
						month_result = today.month - born.month
					else:
						year_result = today.year - born.year
				if year_result:
					animal_list_dict['year_result'] = year_result
				elif month_result:
					animal_list_dict['month_result'] = month_result




				animal_list_dict['id'] = animal_detail.id
				animal_list_dict['animal_tag'] = animal_detail.animal_tag
				animal_list_dict['gender'] = animal_detail.gender
				animal_list_dict['image'] = animal_detail.image
				animal_list_dict['status'] = animal_detail.is_active
				animal_list_dict['animal_type'] = animal_detail.animal_type
				animal_list_dict['animal_breed'] = animal_detail.animal_breed
				all_animal_list.append(animal_list_dict)
			print(all_animal_list)






			return render(request, 'livestock/animal_listing.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_listing.html', locals())


	def post(self,request):
		try:
			male_check =  self.request.POST.get('Male')
			female_check = self.request.POST.get('Female')
			requested_user = User.objects.get(id = request.user.id)
			active_status = self.request.POST.get('active_status')
			retired_category = self.request.POST.get('retired_category')
			milking_status = self.request.POST.get('milking_status')
			dry_female_status = self.request.POST.get('dry_female_status')
			less_than_3_month = self.request.POST.get('less_than_3_month')
			less_than_six = self.request.POST.get('less_than_six')
			less_then_one = self.request.POST.get('less_then_one')
			less_then_one_point_six = self.request.POST.get('less_then_one_point_six')
			more_then_one_pont_six = self.request.POST.get("more_then_one_pont_six")

			if active_status:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Male').order_by('-id')
				print("all_animals")
				return render(request, 'livestock/animal_listing.html', locals())
			if retired_category:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Male').order_by('-id')
				print("all_animals")
				return render(request, 'livestock/animal_listing.html', locals())
			if milking_status:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Male').order_by('-id')
				print("all_animals")
				return render(request, 'livestock/animal_listing.html', locals())
			if less_than_3_month:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Male').order_by('-id')
				print("all_animals")
				return render(request, 'livestock/animal_listing.html', locals())
			if less_than_six:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Male').order_by('-id')
				print("all_animals")
				return render(request, 'livestock/animal_listing.html', locals())
			if less_then_one:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Male').order_by('-id')
				print("all_animals")
				return render(request, 'livestock/animal_listing.html', locals())
			if less_then_one_point_six:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Male').order_by('-id')
				print("all_animals")
				return render(request, 'livestock/animal_listing.html', locals())
			if more_then_one_pont_six:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Male').order_by('-id')
				print("all_animals")
				return render(request, 'livestock/animal_listing.html', locals())


			print("request ", request.POST)

			if male_check:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Male').order_by('-id')
				print("all_animals")
				return render(request, 'livestock/animal_listing.html', locals())
			if female_check:
				all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user, gender = 'Female').order_by('-id')
				print("all_animals", all_animals)
				return render(request, 'livestock/animal_listing.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_listing.html', locals())












from datetime import date
import datetime
from django.utils.timezone import utc

def MinuteHourAgo(time):
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	diff = now - time
	second_diff = diff.seconds
	day_diff = diff.days
	if day_diff < 0:
		return 'dss'

	if day_diff == 0:
		if second_diff < 10:
			return "just now"
		if second_diff < 60:
			return str(int(second_diff)) + " seconds ago"
		if second_diff < 120:
			return "a minute ago"
		if second_diff < 3600:
			return str(int(second_diff / 60)) + " minutes ago"
		if second_diff < 7200:
			return "an hour ago"
		if second_diff < 86400:
			return str(int(second_diff / 3600)) + " hours ago"

	if day_diff == 1:
		return "Yesterday"
	if day_diff < 7:
		return str(int(day_diff)) + " days ago"
	if day_diff < 31:
		return str(int(day_diff / 7)) + " weeks ago"
	if day_diff < 365:
		return str(int(day_diff / 30)) + " months ago"



	return str(day_diff / 365) + " years ago"











class ViewParticluarAnimal(View):

	''' Demonstrate docstring for confirming that this view function will listing all details of user'''

	def get(self,request):
		try:
			product_id = self.request.GET.get('product_id')
			user_obj = User.objects.get(id = int(request.user.id))
			animal_detail = AddedAnimalLiveStock.objects.get(id = int(product_id), created_by = user_obj)
			if type(animal_detail.male_parent) == int:
				male_parent_detail = AddedAnimalLiveStock.objects.filter(id = int(animal_detail.male_parent), created_by = user_obj, gender = 'Male')

			if type(animal_detail.female_parent) == int:
				female_parent_detail =  AddedAnimalLiveStock.objects.filter(id = int(animal_detail.male_parent), created_by = user_obj, gender = 'Female')



			age_str = animal_detail.date_of_birth
			day = age_str.day
			month = age_str.month
			year = age_str.year
			born = date(year, month, day)
			today = date.today()
			year_result = 0
			month_result = 0
			try:
				birthday = born.replace(year = today.year)
			except ValueError:
				birthday = born.replace(year = today.year, month = born.month + 1, day = 1) 
			if birthday > today:
				year_result = today.year - born.year - 1
			else:
				if today.year == born.year:
					month_result = today.month - born.month
				else:
					year_result = today.year - born.year









			male_parent = AddedAnimalLiveStock.objects.filter(gender = 'Male').values('animal_tag', 'id').exclude(id = int(product_id))
			female_parent = AddedAnimalLiveStock.objects.filter(gender = 'Female').values('animal_tag','id').exclude(id = int(product_id))
			all_child_parents = AddedAnimalLiveStock.objects.values('animal_tag','id').exclude(id = int(product_id))


			child_already_list = ParentsChild.objects.filter(animal_instance = animal_detail, created_by = user_obj)
			list_of_childs = []
			for one_record in child_already_list:
				new_dict = {}
				one_id = int(one_record.child_id)
				new_dict['id'] = one_record.id
				one_object = AddedAnimalLiveStock.objects.get(id = one_id, created_by = user_obj)
				new_dict['one_object'] = one_object

				list_of_childs.append(new_dict)



			dropdown_child_already_list = ParentsChild.objects.filter(animal_instance = animal_detail, created_by = user_obj).values_list('child_id', flat = True)
			make_list_int = list(map(int,dropdown_child_already_list))



			all_health_record = HeathInformation.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail)


			######make time interval
			all_health_record_list = []

			for one_time in all_health_record:
				my_health = {}
				created_on = one_time.created_on

				ago = MinuteHourAgo(created_on)
				my_health['ago'] = ago
				my_health['tag_name'] = one_time.tag_name
				my_health['cost_amount'] = one_time.cost_amount
				my_health['id'] = one_time.id
				my_health['text_description'] = one_time.text_description
				all_health_record_list.append(my_health)








			all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail)

			all_milking_record_list = []
			for one_milk in all_milking_record:
				milk_dict = {}
				milk_dict['morning_time'] = one_milk.morning_time
				milk_dict['id'] = one_milk.id
				milk_dict['evening_time'] = one_milk.evening_time
				milk_dict['sum_of_one'] = int(one_milk.morning_time) + int(one_milk.evening_time)
				milk_dict['created_on'] = one_milk.created_on
				all_milking_record_list.append(milk_dict)

			all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail).values_list('morning_time', flat = True)


			all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail).values_list('evening_time', flat = True)

			all_milking_record_morning = list(map(int, all_milking_record_morning))
			all_milking_record_evening = list(map(int, all_milking_record_evening))


			sum_of_morning = sum(all_milking_record_morning)
			sum_of_evening = sum(all_milking_record_evening)

			sum_of_two_list = sum(all_milking_record_evening) + sum(all_milking_record_morning)


			filter_by = request.GET.get('filter')
			if filter_by:
				if int(filter_by) == 7:
					some_day_last_week = timezone.now().date() - timedelta(days=7)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail, created_on__gte = some_day_last_week)

					all_milking_record_list = []
					for one_milk in all_milking_record:
						milk_dict = {}
						milk_dict['morning_time'] = one_milk.morning_time
						milk_dict['id'] = one_milk.id
						milk_dict['evening_time'] = one_milk.evening_time
						milk_dict['sum_of_one'] = int(one_milk.morning_time) + int(one_milk.evening_time)
						milk_dict['created_on'] = one_milk.created_on
						all_milking_record_list.append(milk_dict)

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week, animal_instance = animal_detail).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week,animal_instance = animal_detail).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)

					sum_of_two_list = sum(all_milking_record_evening) + sum(all_milking_record_morning)
					filter_by_class = int(7)


				elif int(filter_by) == 30:
					filter_by_class = 30
					some_day_last_month = timezone.now().date() - timedelta(days=30)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail, created_on__gte = some_day_last_month)

					all_milking_record_list = []
					for one_milk in all_milking_record:
						milk_dict = {}
						milk_dict['morning_time'] = one_milk.morning_time
						milk_dict['id'] = one_milk.id
						milk_dict['evening_time'] = one_milk.evening_time
						milk_dict['sum_of_one'] = int(one_milk.morning_time) + int(one_milk.evening_time)
						milk_dict['created_on'] = one_milk.created_on
						all_milking_record_list.append(milk_dict)

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_month,animal_instance = animal_detail).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_month, animal_instance = animal_detail).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)

					sum_of_two_list = sum(all_milking_record_evening) + sum(all_milking_record_morning)

				elif int(filter_by) == 91:
					filter_by_class = 91
					some_day_last_week = timezone.now().date() - timedelta(days=91)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail, created_on__gte = some_day_last_week)

					all_milking_record_list = []
					for one_milk in all_milking_record:
						milk_dict = {}
						milk_dict['morning_time'] = one_milk.morning_time
						milk_dict['id'] = one_milk.id
						milk_dict['evening_time'] = one_milk.evening_time
						milk_dict['sum_of_one'] = int(one_milk.morning_time) + int(one_milk.evening_time)
						milk_dict['created_on'] = one_milk.created_on
						all_milking_record_list.append(milk_dict)

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week, animal_instance = animal_detail).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week, animal_instance = animal_detail).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)

					sum_of_two_list = sum(all_milking_record_evening) + sum(all_milking_record_morning)

				elif int(filter_by) == 184:
					filter_by_class = 184
					some_day_last_week = timezone.now().date() - timedelta(days=184)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail, created_on__gte = some_day_last_week)

					all_milking_record_list = []
					for one_milk in all_milking_record:
						milk_dict = {}
						milk_dict['morning_time'] = one_milk.morning_time
						milk_dict['id'] = one_milk.id
						milk_dict['evening_time'] = one_milk.evening_time
						milk_dict['sum_of_one'] = int(one_milk.morning_time) + int(one_milk.evening_time)
						milk_dict['created_on'] = one_milk.created_on
						all_milking_record_list.append(milk_dict)

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week, animal_instance = animal_detail).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week, animal_instance = animal_detail).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)

					sum_of_two_list = sum(all_milking_record_evening) + sum(all_milking_record_morning)

				elif int(filter_by) == 365:
					filter_by_class = 365
					some_day_last_week = timezone.now().date() - timedelta(days=365)
					all_milking_record = MilKLitre.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail, created_on__gte = some_day_last_week)

					all_milking_record_list = []
					for one_milk in all_milking_record:
						milk_dict = {}
						milk_dict['morning_time'] = one_milk.morning_time
						milk_dict['id'] = one_milk.id
						milk_dict['evening_time'] = one_milk.evening_time
						milk_dict['sum_of_one'] = int(one_milk.morning_time) + int(one_milk.evening_time)
						milk_dict['created_on'] = one_milk.created_on
						all_milking_record_list.append(milk_dict)

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week, animal_instance = animal_detail).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week, animal_instance = animal_detail).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)

					sum_of_two_list = sum(all_milking_record_evening) + sum(all_milking_record_morning)




			all_gallery = AllGalleryAddedByUser.objects.filter(product = animal_detail)

			all_description = DescriptionTable.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail)
			all_description_list = []

			for one_desc in all_description:
				one_dict = {}
				one_dict['description'] = one_desc.description

				created_on = one_desc.created_on
				ago = MinuteHourAgo(created_on)


				one_dict['created_on'] = ago
				one_dict['id'] = one_desc.id
				all_description_list.append(one_dict)

			print(all_milking_record_list)



			return render(request, 'livestock/animal_info.html', locals())
		except Exception as e:
			print("\n" * 3)
			print(e)
			print("\n" * 3)

			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())




class UpdateExactAnimalDetail(View):


	def post(self,request):
		context = {}

		try :

			user_id = request.user.id
			user_obj = User.objects.get(id = user_id)
			animal_tag = request.POST.get('animal_tag')
			hidden_id = request.POST.get('animal_particular_id')
			age = request.POST.get('age')
			animal_bread = request.POST.get('animal_bread')
			gender = request.POST.get('gender')
			import dateparser
			age = dateparser.parse(age)

			animal_type = self.request.POST.get('animal_type')
			image = request.FILES.get('main_image')
			obj = AddedAnimalLiveStock.objects.get(id = int(hidden_id),created_by = user_obj)
			print("ddddddddddddddd->", obj)
			if not image:
				image = obj.image


			obj.image = image
			obj.animal_tag  = animal_tag
			obj.animal_breed  = animal_bread
			obj.gender  = gender
			obj.animal_type  = animal_type
			obj.updated_by  = user_obj

			print(age)
			obj.date_of_birth=age
			obj.save()

			context['status']  = 200
			context['message'] = 'You have successfully Update Your Animal'
			return HttpResponse(json.dumps(context))
		except Exception as e:
			print(e)
			context['status'] = 500
			context['error_message'] = 'Something went wrong,Please try again later or contact us'
			return HttpResponse(json.dumps(context))











class AddHealthAnimalDetail(View):


	def post(self,request):
		context = {}

		try :
			user_id = request.user.id
			animal_id = request.POST.get('animal_particular_id')
			get_animal_instance = AddedAnimalLiveStock.objects.get(id = int(animal_id))
			user_obj = User.objects.get(id = user_id)
			animal_tag = request.POST.get('title_health')
			cost = request.POST.get('cost')
			description = request.POST.get('description')
			HeathInformation.objects.create(animal_instance = get_animal_instance, cost_amount=cost, tag_name = animal_tag, text_description = description,created_by = user_obj)

			context['status']  = 200
			context['message'] = 'You have successfully Add an Health Expenses of this Animal'
			return HttpResponse(json.dumps(context))
		except Exception as e:
			print(e)
			context['status'] = 500
			context['error_message'] = 'Something went wrong,Please try again later or contact us'
			return HttpResponse(json.dumps(context))




class AddGalleryMore(View):


	def post(self,request):
		context = {}

		try :
			user_id = request.user.id
			user_obj = User.objects.get(id = user_id)

			animal_particular_id = request.POST.get('animal_particular_id')
			image = request.FILES.get('main_image')
			get_animal_instance = AddedAnimalLiveStock.objects.get(id = int(animal_particular_id))

			AllGalleryAddedByUser.objects.create(image = image,product = get_animal_instance)

			context['status']  = 200
			context['message'] = 'You have successfully Added an Gallery Image of Your Animal'
			return HttpResponse(json.dumps(context))
		except Exception as e:
			print(e)
			context['status'] = 500
			context['error_message'] = 'Something went wrong,Please try again later or contact us'
			return HttpResponse(json.dumps(context))








class AddMilkingAnimal(View):


	def post(self,request):
		context = {}

		try :
			user_id = request.user.id
			user_obj = User.objects.get(id = user_id)
			hidden_id = request.POST.get('animal_particular_id')
			get_animal_instance = AddedAnimalLiveStock.objects.get(id = int(hidden_id))



			morning_time = request.POST.get('morning_time')
			evening_time = self.request.POST.get('evening_time')
			MilKLitre.objects.create(animal_instance = get_animal_instance, morning_time=morning_time, 
				evening_time = evening_time,created_by = user_obj)

			context['status']  = 200
			context['message'] = 'You have successfully Added an Milking Record of Your Animal'
			return HttpResponse(json.dumps(context))
		except Exception as e:
			print(e)
			context['status'] = 500
			context['error_message'] = 'Something went wrong,Please try again later or contact us'
			return HttpResponse(json.dumps(context))




class AddChildParent(View):


	def post(self,request):
		context = {}

		try :
			user_id = request.user.id
			user_obj = User.objects.get(id = user_id)
			hidden_id = request.POST.get('family_particular_id')
			get_animal_instance = AddedAnimalLiveStock.objects.get(id = int(hidden_id))



			male_parent = request.POST.get('male_parent')
			female_parent = self.request.POST.get('female_parent')
			if male_parent:
				get_animal_instance.male_parent = male_parent
				get_animal_instance.save()
			if female_parent:
				get_animal_instance.female_parent = female_parent
				get_animal_instance.save()

			child_select = self.request.POST.getlist('child_select[]')
			for one in child_select:
				ParentsChild.objects.create(animal_instance = get_animal_instance, child_id = one, created_by = user_obj)



			context['status']  = 200
			context['message'] = 'You have successfully Added an Family Members of Your Animal'
			return HttpResponse(json.dumps(context))
		except Exception as e:
			print(e)
			context['status'] = 500
			context['error_message'] = 'Something went wrong,Please try again later or contact us'
			return HttpResponse(json.dumps(context))








class AddDescriptionAnimal(View):


	def post(self,request):
		context = {}

		try :
			user_id = request.user.id
			user_obj = User.objects.get(id = user_id)
			animal_particular_id = request.POST.get('animal_particular_id')
			get_animal_instance = AddedAnimalLiveStock.objects.get(id = int(animal_particular_id))
			description = request.POST.get('description')
			DescriptionTable.objects.create(animal_instance = get_animal_instance, description=description, created_by = user_obj)

			context['status']  = 200
			context['message'] = 'You have successfully Added an Description of Your Animal'
			return HttpResponse(json.dumps(context))
		except Exception as e:
			print(e)
			context['error_message'] = 500
			context['status'] = 'Something went wrong,Please try again later or contact us'
			return HttpResponse(json.dumps(context))






class DeactivateAnimal(View):

	def get(self,request):
		context = {}
		try:
			user_obj = User.objects.get(id = request.user.id)
			id_animal = self.request.GET.get('id')
			animal_instance = AddedAnimalLiveStock.objects.get(id = int(id_animal), created_by = user_obj)

			if animal_instance.is_active == True:
				animal_instance.is_active = False
				animal_instance.save()
				
				context['status'] = 'success'
				context['msg'] = 'True status'
				return HttpResponse(json.dumps(context))


			elif animal_instance.is_active == False:
				animal_instance.is_active = True
				animal_instance.save()
				context['status'] = 'success'
				context['msg'] = 'False status'
				return HttpResponse(json.dumps(context))
		except Exception as e:
			print(e)
			context['status'] = 'fail'
			context['msg'] = 'something went wrong'
			return HttpResponse(json.dumps(context))



























class DeleteHealth(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			delete_health = self.request.GET.get('title_id')
			product_obj = HeathInformation.objects.get(id  = delete_health,created_by = user_obj)
			product_id = int(product_obj.animal_instance.id)
			HeathInformation.objects.filter(id = int(delete_health),created_by = user_obj).delete()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())


class DeleteMilk(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			milk_id = self.request.GET.get('milk_id')
			product_obj = MilKLitre.objects.get(id  = int(milk_id))
			product_id = int(product_obj.animal_instance.id)
			MilKLitre.objects.filter(id =int(milk_id) ,created_by = user_obj).delete()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())



class DeleteDescription(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			delete_desc_id = self.request.GET.get('delete_desc_id')
			product_obj = DescriptionTable.objects.get(id  = int(delete_desc_id))
			product_id = int(product_obj.animal_instance.id)
			DescriptionTable.objects.filter(id = int(delete_desc_id),created_by = user_obj).delete()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())











class DeleteImageTab(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			delete_desc_id = self.request.GET.get('image_id')
			product_obj = AllGalleryAddedByUser.objects.get(id  = int(delete_desc_id))
			product_id = int(product_obj.product.id)
			AllGalleryAddedByUser.objects.filter(id = int(delete_desc_id),product__created_by = user_obj).delete()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())













class DeleteMaleParent(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			delete_male_id = self.request.GET.get('delete_male_id')
			product_obj = AddedAnimalLiveStock.objects.get(id  = int(delete_male_id), created_by = user_obj)
			print("dddddddddddddddddddddddddddddd", product_obj)
			product_id = int(product_obj.id)
			product_obj.male_parent = ''
			product_obj.save()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())






class DeleteFemaleParent(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			delete_female_id = self.request.GET.get('delete_female_id')
			product_obj = AddedAnimalLiveStock.objects.get(id  = int(delete_female_id), created_by = user_obj)
			product_id = int(product_obj.id)
			product_obj.male_parent = ''
			product_obj.save()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())






class DeleteChildObject(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			delete_child_id = self.request.GET.get('delete_child_id')
			product_obj = ParentsChild.objects.get(id  = int(delete_child_id))
			product_id = int(product_obj.animal_instance.id)
			ParentsChild.objects.filter(id = int(delete_child_id),created_by = user_obj).delete()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())






