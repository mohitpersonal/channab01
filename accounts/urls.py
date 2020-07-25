from .views import RegisterView,AddAnimalLivestock,ViewParticluarAnimal,ListingAnimalLiveStock,LoginView,LogoutView,ForgetView,ResetPassword
from django.urls import path
from django.contrib.auth.decorators import login_required




urlpatterns = [
	
	##### related to register page function

	path('register/', RegisterView.as_view(), name = 'RegisterView'),
	path('login/', LoginView.as_view(), name = 'LoginView'),
	path('forget/', ForgetView.as_view(), name = 'ForgetView'),
	path('reset_psw/', ResetPassword.as_view(), name = 'ResetPassword'),
	path('logout/', LogoutView.as_view(), name = 'LogoutView'),


	####### livestock module

	path('add_animal/', login_required(AddAnimalLivestock.as_view()), name = 'AddAnimalLivestock'),
	path('animal_list/', login_required(ListingAnimalLiveStock.as_view()), name = 'ListingAnimalLiveStock'),
	path('view_animal/', login_required(ViewParticluarAnimal.as_view()), name = 'ViewParticluarAnimal')


]