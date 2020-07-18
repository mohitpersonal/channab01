from .views import RegisterView,LoginView,LogoutView
from django.urls import path


urlpatterns = [
	
	##### related to register page function

	path('register/', RegisterView.as_view(), name = 'RegisterView'),
	path('login/', LoginView.as_view(), name = 'LoginView'),
	path('logout/', LogoutView.as_view(), name = 'LogoutView')

]