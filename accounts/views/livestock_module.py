from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from accounts.models import AddedAnimalLiveStock,AllGalleryAddedByUser,HeathInformation,MilKLitre,DescriptionTable
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

			print("\n" * 3)
			print("images is --------->", image)
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
			requested_user = User.objects.get(id = request.user.id)
			all_animals = AddedAnimalLiveStock.objects.filter(created_by = requested_user).order_by('-id')

			print("all_animals->", all_animals[0].image)
			return render(request, 'livestock/animal_listing.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_listing.html', locals())








from datetime import date
  
# def calculateAge(born): 
#     today = date.today()
#     try:  
#         birthday = born.replace(year = today.year)
#         print(birthday)
#     except ValueError:  
#         birthday = born.replace(year = today.year, 
#                   month = born.month + 1, day = 1) 
  
#     if birthday > today: 
#     	return today.year - born.year - 1
#     else:
#     	if today.year == born.year:
#     		month = today.month - born.month
#     		return month
#         return today.year - born.year 



from datetime import datetime
import datetime
def MinuteHourAgo(time):
	now = datetime.datetime.now()

	print(now)
	print(time)
	diff = now - time
	return diff








class ViewParticluarAnimal(View):

	''' Demonstrate docstring for confirming that this view function will listing all details of user'''

	def get(self,request):
		try:
			product_id = self.request.GET.get('product_id')
			user_obj = User.objects.get(id = int(request.user.id))
			animal_detail = AddedAnimalLiveStock.objects.get(id = int(product_id), created_by = user_obj)



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





			male_parent = AddedAnimalLiveStock.objects.filter(gender = 'Male').values_list('animal_tag', flat = True)
			female_parent = AddedAnimalLiveStock.objects.filter(gender = 'Female').values_list('animal_tag', flat = True)
			all_child_parents = AddedAnimalLiveStock.objects.filter(is_active = True).values_list('animal_tag', flat = True)


			all_health_record = HeathInformation.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail)


			######make time interval
			# all_health_record_list = []

			# for one_time in all_health_record:
			# 	created_on = one_time.created_on
				
			# 	ago = MinuteHourAgo(created_on)
				# all_health_record_list.append(ago)


			# print("\n" * 3)
			# print("all_milking_record_list is ------>", all_health_record_list)
			# print("\n" * 3)






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

			all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj).values_list('morning_time', flat = True)


			all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj).values_list('evening_time', flat = True)

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

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week).values_list('evening_time', flat = True)

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

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_month).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_month).values_list('evening_time', flat = True)

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

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week).values_list('evening_time', flat = True)

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

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week).values_list('evening_time', flat = True)

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

					all_milking_record_morning = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week).values_list('morning_time', flat = True)


					all_milking_record_evening = MilKLitre.objects.filter(is_active = True, created_by = user_obj,created_on__gte = some_day_last_week).values_list('evening_time', flat = True)

					all_milking_record_morning = list(map(int, all_milking_record_morning))
					all_milking_record_evening = list(map(int, all_milking_record_evening))


					sum_of_morning = sum(all_milking_record_morning)
					sum_of_evening = sum(all_milking_record_evening)

					sum_of_two_list = sum(all_milking_record_evening) + sum(all_milking_record_morning)




			all_gallery = AllGalleryAddedByUser.objects.filter(product = animal_detail)

			all_description = DescriptionTable.objects.filter(is_active = True, created_by = user_obj, animal_instance = animal_detail).values('description','created_on', 'id')

			print(all_description)


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
			animal_type = self.request.POST.get('animal_type')
			image = request.FILES.get('main_image')
			obj = AddedAnimalLiveStock.objects.get(id = int(hidden_id),created_by = user_obj)

			print("\n" * 3)
			print("image is ---------->", image)
			print("\n" * 3)
			if not image:
				image = obj.image
			

			AddedAnimalLiveStock.objects.filter(id = int(hidden_id),created_by = user_obj).update(animal_tag = animal_tag, date_of_birth=age, animal_breed = animal_bread, gender = gender, animal_type = animal_type,updated_by = user_obj)

			obj.image = image
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
			id_animal = self.request.GET.get('id')
			animal_instance = AddedAnimalLiveStock.objects.get(id = int(id_animal))

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
		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			context['msg'] = 'something went wrong'
			return HttpResponse(json.dumps(context))



























class DeleteHealth(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			delete_health = self.request.GET.get('title_id')
			product_obj = HeathInformation.objects.get(id  = delete_health)
			product_id = int(product_obj.animal_instance.id)
			HeathInformation.objects.filter(id = delete_health,created_by = user_obj).delete()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())


class DeleteMilk(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			milk_id = self.request.GET.get('milk_id')
			product_obj = MilKLitre.objects.get(id  = milk_id)
			product_id = int(product_obj.animal_instance.id)
			MilKLitre.objects.filter(id = milk_id,created_by = user_obj).delete()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())



class DeleteDescription(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			delete_desc_id = self.request.GET.get('delete_desc_id')
			product_obj = DescriptionTable.objects.get(id  = delete_desc_id)
			product_id = int(product_obj.animal_instance.id)
			DescriptionTable.objects.filter(id = delete_desc_id,created_by = user_obj).delete()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())











class DeleteImageTab(View):

	def get(self,request):

		try:
			request_user = self.request.user.id
			user_obj = User.objects.get(id = request_user)
			delete_desc_id = self.request.GET.get('delete_desc_id')
			product_obj = AllGalleryAddedByUser.objects.get(id  = delete_desc_id)
			product_id = int(product_obj.animal_instance.id)
			AllGalleryAddedByUser.objects.filter(id = delete_desc_id,created_by = user_obj).delete()
			return redirect('/accounts/view_animal/?product_id={}'.format(product_id))

		except:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'livestock/animal_info.html', locals())

