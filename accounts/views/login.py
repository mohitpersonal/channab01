from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import messages
import random
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login
from accounts.models import UserProfileInfo

class LoginView(View):

	''' Demonstrate docstring for confirming that this view function will login a user'''

	def get(self,request):

		try:
			if request.user.is_authenticated:
				return redirect('/')
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





class ForgetView(View):
    def post(self, request):
        try :
            mobile_number = request.POST.get('mobile_number').strip()
            check_exist = User.objects.filter(email = mobile_number)
            if check_exist :
                random_otp = ''.join(random.choice("1234567890") for _ in range(6))
                client_instance = UserProfileInfo.objects.get(user = check_exist[0])
                client_instance.otp_password = random_otp
                client_instance.save()
                messages.success(request, 'we will send you an message with instructions on how to reset your password')
            else:
                messages.error(request,'No user account registered with provided information. Please check your details and try again')
            return render(request, 'accounts/forgot-password.html', locals())
        except Exception as e:
            print(e)
            messages.error(request,'Something went wrong, Please try again later')
            return render(request, 'accounts/forgot-password.html',locals())
    def get(self,request):
        try:
            if request.user.is_authenticated:
                return redirect('/')
            else:
                return render(request,'secret/forgot-password.html', locals())
        except:
            return render(request,'accounts/forgot-password.html')

class ResetPassword(View):

    def get(self,request):
        try:
            email = request.GET.get('q')
            check_obj = User.objects.get(email = email)

            return render(request,'accounts/reset_password.html', locals())
        except:
            return render(request,'accounts/reset_password.html')

    def post(self,request):
        try:
            mobile_number = request.POST.get('mobile_number')
            check_obj = User.objects.get(email = mobile_number)
            otp_obj = UserProfileInfo.objects.filter(user = check_obj)
            saved_otp = otp_obj[0].otp_password
            if request.method == 'POST':
                password = request.POST.get('password')
                entered_otp = request.POST.get('otp')
                if saved_otp == entered_otp:
                	check_obj.set_password(password)
                	check_obj.save()
                	messages.success(request, 'Your password is Updated Successfully! Please Login Here')
                	UserProfileInfo.objects.filter(user = check_obj).update(otp_password = '')
                	return HttpResponseRedirect('/accounts/login/')
                else:
                    messages.error(request,'Please check your entered verification code')

            email = email
            return render(request, 'accounts/reset_password.html',locals())
        except:
            messages.error(request,'Something went wrong, Please try again later')
        return render(request, 'accounts/reset_password.html',locals())

	 