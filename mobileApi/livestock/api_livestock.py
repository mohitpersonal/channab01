from django.http import HttpResponse
from product.models import Product,PriceFilter,Category,MarketAddByAdmin,CommentReviewsStar,ProductMarket, ProductImage
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
import ast,sys,json
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
import string, random
from accounts.models import UserProfileInfo,AllGalleryAddedByUser,AddedAnimalLiveStock
from django.contrib.auth import authenticate, logout, login


class RegisterView(APIView):

	''' Demonstrate docstring for confirming that this view api will register a user'''


	def post(self, request):
		try:
			context = {}
			api_key = settings.API_KEY_FOR_SECURITY
			print(request.META.get('HTTP_X_API_KEY'))
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))

			mobile_number = self.request.POST.get('mobile_number')
			if not mobile_number:
				context['message'] = 'Please Fill out Your Mobile Number'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
			elif mobile_number:
				if len(mobile_number) < 8:
					context['message'] = 'Mobile Number must contains more than 8 Characters'
					context['status'] = 200
					return HttpResponse(json.dumps(context))


			password = self.request.POST.get('password')
			if not password:
				context['message'] = 'Please Fill out Your Password'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
			elif password:
				if len(password) <= 6:
					context['message'] = 'Password must contains more than 6 Characters'
					context['status'] = 200
					return HttpResponse(json.dumps(context))


			email = self.request.POST.get('email')
			if email:
				email = email.strip().lower()

            # make obj of class to save register info
			check_user_mobile = User.objects.filter(username= mobile_number).count()

			if check_user_mobile > 0:
				context['message'] = 'Sorry,This Mobile Number is already in Use'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
				
			else:
				user_obj = User.objects.create(email=mobile_number, username = mobile_number)
				user_obj.set_password(password)
				user_obj.save()
				letters = string.ascii_lowercase + string.ascii_uppercase +  string.digits 
				user_token = ''.join(random.choice(letters) for _ in range(35))
				UserProfileInfo.objects.create(user = user_obj,token_for_user = user_token, active = True)
				context['message'] = 'Thank you for your registration! Your account has been successfully created. An Verification Code has been sent to you with detailed instructions on how to activate it'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
		except :
			context = {}
			print(sys.exc_info())
			context['message'] = 'An error occurred in registering your account, please try again or contact us'
			context['status'] = 500
			return HttpResponse(json.dumps(context))









class ApiLoginView(APIView):

	''' Demonstrate docstring for confirming that this view function will login a user'''

	def post(self, request):
		try:
			context = {}
			api_key = settings.API_KEY_FOR_SECURITY
			print(request.META.get('HTTP_X_API_KEY'))
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))

			mobile_number = self.request.POST.get('mobile_number')
			if not mobile_number:
				context['message'] = 'Please Fill out Your Mobile Number'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
			password = self.request.POST.get('password')
			if not password:
				context['message'] = 'Please Fill out Your Password'
				context['status'] = 200
				return HttpResponse(json.dumps(context))

			mobile_exist = User.objects.filter(username = mobile_number).count()

			if mobile_exist > 0:
				user_obj = User.objects.get(email = mobile_number)
				if user_obj.is_active == 1:
					username = User.objects.get(email = mobile_number)
					user = authenticate(username = username, password = password)
					if user is not None:
						login(request, user)
						context['message'] =  'Login SuccessFully'
						context['status'] = 200
						return HttpResponse(json.dumps(context))
						
					else :
						context['message'] =  'Incorrect password, please try again'
						context['status'] = 200
						return HttpResponse(json.dumps(context))
				else:
					context['message'] =  'Sorry, You have not confirmed or active your account'
					context['status'] = 200
					return HttpResponse(json.dumps(context))
			else:
				context['message'] =  'Incorrect Mobile Number or password, please try again'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
		except Exception as e:
			print(e)
			context = {}
			context['message'] = 'Something Went Wrong,Please try again later'
			context['status'] = 500
			return HttpResponse(json.dumps(context))





class ApiLogoutView(APIView):

    '''demonstarte docstring for confirm that this api is used for logout an user'''

    def get(self,request):
        try:
        	context = {}
        	api_key = settings.API_KEY_FOR_SECURITY
        	print(request.META.get('HTTP_X_API_KEY'))
        	token_From_request = request.META.get('HTTP_X_API_KEY')
        	if api_key != token_From_request:
        		context['message'] = 'Bad Request,Token Not Found!'
        		context['status'] = 403
        		return HttpResponse(json.dumps(context))

        	logout(request)
        	context['message'] =  'Logout SuccessFully'
        	context['status'] = 200
        	return HttpResponse(json.dumps(context))
        except:
        	print(sys.exc_info())
        	context = {}
        	context['message'] = 'Something Went Wrong,Please try again later'
        	context['status'] = 500
        	return HttpResponse(json.dumps(context))








class ForgetView(APIView):

    def post(self, request):
        try :
        	context = {}
        	api_key = settings.API_KEY_FOR_SECURITY
        	print(request.META.get('HTTP_X_API_KEY'))
        	token_From_request = request.META.get('HTTP_X_API_KEY')
        	if api_key != token_From_request:
        		context['message'] = 'Bad Request,Token Not Found!'
        		context['status'] = 403
        		return HttpResponse(json.dumps(context))

        	mobile_number = request.POST.get('mobile_number')
        	if not mobile_number:
        		context['message'] = 'Please Fill out Your Mobile Number'
        		context['status'] = 200
        		return HttpResponse(json.dumps(context))

        	check_exist = User.objects.filter(email = mobile_number)
        	if check_exist :
        		random_otp = ''.join(random.choice("1234567890") for _ in range(6))
        		client_instance = UserProfileInfo.objects.get(user = check_exist[0])
        		client_instance.otp_password = random_otp
        		client_instance.save()
        		context['message'] =  'we will send you an message with instructions on how to reset your password'
        		context['status'] = 200
        		return HttpResponse(json.dumps(context))
        	else:
        		context['message'] =  'No user account registered with provided information. Please check your details and try again'
        		context['status'] = 200
        		return HttpResponse(json.dumps(context))
        except Exception as e:
        	print(e)
        	context = {}
        	context['message'] = 'Something Went Wrong,Please try again later'
        	context['status'] = 500
        	return HttpResponse(json.dumps(context))

class ResetPassword(APIView):


    def post(self,request):
        try:
        	context = {}
        	api_key = settings.API_KEY_FOR_SECURITY
        	print(request.META.get('HTTP_X_API_KEY'))
        	token_From_request = request.META.get('HTTP_X_API_KEY')
        	if api_key != token_From_request:
        		context['message'] = 'Bad Request,Token Not Found!'
        		context['status'] = 403
        		return HttpResponse(json.dumps(context))
        	mobile_number = request.POST.get('mobile_number')
        	if not mobile_number:
        		context['message'] = 'Please Fill out Your Mobile Number'
        		context['status'] = 200
        		return HttpResponse(json.dumps(context))


        	check_obj = User.objects.get(email = mobile_number)
        	otp_obj = UserProfileInfo.objects.filter(user = check_obj)
        	saved_otp = otp_obj[0].otp_password
        	password = request.POST.get('password')
        	entered_otp = request.POST.get('otp')
        	if saved_otp == entered_otp:
        		check_obj.set_password(password)
        		check_obj.save()
        		context['message'] = 'Your password is Updated Successfully! Please Login Here'
        		context['status'] = 200
        		UserProfileInfo.objects.filter(user = check_obj).update(otp_password = '')
        		return HttpResponse(json.dumps(context))
        	else:
        		context['message'] = 'Please check your entered verification code'
        		context['status'] = 200
        		return HttpResponse(json.dumps(context))
        except:
        	context = {}
        	context['message'] = 'Something Went Wrong,Please try again later'
        	context['status'] = 500
        	return HttpResponse(json.dumps(context))
            

###########


class APiAnimalLivestock(APIView):

	''' Demonstrate docstring for confirming that this view function will used to add an animal by user'''

	def post(self,request):
		try:
			context = {}
			api_key = settings.API_KEY_FOR_SECURITY
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))

			animal_tag = request.POST.get('animal_tag')
			if not animal_tag:
				context['message'] = 'Please Fill out Your Animal Tag'
				context['status'] = 200
				return HttpResponse(json.dumps(context))

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
			if not image:
				context['message'] = 'Image is required'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
			if not animal_bread:
				context['message'] = 'Please Select any Animal Breed'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
			if not category:
				context['message'] = 'Please Select any Animal Category'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
			if not gender:
				context['message'] = 'Please Select any Gender'
				context['status'] = 200
				return HttpResponse(json.dumps(context))
			if not animal_type:
				context['message'] = 'Please any Animal Type'
				context['status'] = 200
				return HttpResponse(json.dumps(context))

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

			context['message'] = 'An animal has been successfully registered for sale purpose.'
			context['status'] = 200
			return HttpResponse(json.dumps(context))
			
		except Exception as e:
			print(e)
			context = {}
			context['message'] = 'Something Went Wrong,Please try again later'
			context['status'] = 500
			return HttpResponse(json.dumps(context))
            


