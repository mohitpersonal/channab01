from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
import string,random
from accounts.models import UserProfileInfo



class RegisterView(View):

	''' Demonstrate docstring for confirming that this view function will register a user'''

	def get(self,request):

		try:
			if request.user.is_authenticated:
				return redirect('/')

			return render(request, 'accounts/register.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'accounts/register.html', locals())

	def post(self, request):
		try:
			mobile_number = self.request.POST.get('mobile_number')
			password = self.request.POST['password'].strip()
			email = self.request.POST.get('email')
			if email:
				email = email.strip().lower()

            # make obj of class to save register info
			check_user_mobile = User.objects.filter(username= mobile_number).count()
			if check_user_mobile > 0:
				messages.error(request, 'User already exist with Entered Mobile Number')
				return render(request, 'user/register.html')
			else:
				user_obj = User.objects.create(email=mobile_number, username = mobile_number)
				user_obj.set_password(password)
				user_obj.save()
				letters = string.ascii_lowercase + string.ascii_uppercase +  string.digits 
				user_token = ''.join(random.choice(letters) for _ in range(35))
				UserProfileInfo.objects.create(user = user_obj,token_for_user = user_token, active = True)
				messages.success(request,'Thank you for your registration! Your account has been successfully created. An Verification Code has been sent to you with detailed instructions on how to activate it')
				return render(request, 'accounts/register.html', locals())
		except :
			messages.error(request,'An error occurred in registering your account, please try again or contact us')
			return render(request, 'accounts/register.html', locals())

