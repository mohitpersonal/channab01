from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login


class LoginView(View):

	''' Demonstrate docstring for confirming that this view function will login a user'''

	def get(self,request):

		try:
			return render(request, 'accounts/login.html', locals())
		except Exception as e:
			print(e)
			messages.error(request,'Something went wrong,Please try again later or contact us')
			return render(request, 'accounts/login.html', locals())

	def post(self, request):
		try:
			mobile_number = self.request.POST.get('mobile_number').strip()
			# next_ = self.request.POST.get('next_').strip()
			password = self.request.POST.get('password')
			mobile_exist = User.objects.filter(username = mobile_number).count()

			if mobile_exist > 0:
				user_obj = User.objects.get(email = mobile_number)
				if user_obj.is_active == 1:
					username = User.objects.get(email = mobile_number)
					user = authenticate(username = username, password = password)
					if user is not None:
						login(request, user)
						return redirect('/')
					else :
						messages.error(request,'Incorrect password, please try again')
						return render(request, 'accounts/login.html',locals())
				else:
					messages.error(request,'Sorry, You have not confirmed or active your account')
					return render(request, 'accounts/login.html',locals())
			else:
				messages.error(request,'Incorrect Mobile Number or password, please try again')
				return render(request, 'accounts/login.html',locals())
		except Exception as e:
			print("\n" * 3)
			print(e)
			print("\n" * 3)
			messages.error(request,'Something Went Wrong,Please try again later')
			return render(request, 'accounts/login.html',locals())



class LogoutView(View):

    '''demonstarte docstring for confirm that this function is used for logout an user'''

    def get(self,request):
        try:
            logout(request)
            return redirect('/accounts/login/')
        except:
            pass


