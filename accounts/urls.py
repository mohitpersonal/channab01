from .views import *
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

	path('update_animal_detail/', login_required(UpdateExactAnimalDetail.as_view()), name = 'UpdateExactAnimalDetail'),
	path('add_animal/', login_required(AddAnimalLivestock.as_view()), name = 'AddAnimalLivestock'),
	path('animal_list/', login_required(ListingAnimalLiveStock.as_view()), name = 'ListingAnimalLiveStock'),
	path('view_animal/', login_required(ViewParticluarAnimal.as_view()), name = 'ViewParticluarAnimal'),
	path('deactivate_animal/', login_required(DeactivateAnimal.as_view()), name = 'DeactivateAnimal'),


	####animal_details page
	path('added_animal_milking/', login_required(AddMilkingAnimal.as_view()), name = 'AddMilkingAnimal'),
	path('milk_delete/', login_required(DeleteMilk.as_view()), name = 'DeleteMilk'),



	###description
	path('description_added/', login_required(AddDescriptionAnimal.as_view()), name = 'AddDescriptionAnimal'),
	path('delete_description/', login_required(DeleteDescription.as_view()), name = 'DeleteDescription'),

	## gallery
	path('add_gallery/', login_required(AddGalleryMore.as_view()), name = 'AddGalleryMore'),
	path('delete_image/', login_required(DeleteImageTab.as_view()), name = 'DeleteImageTab'),

	### health edit more
	path('add_animal_detail/', login_required(AddHealthAnimalDetail.as_view()), name = 'AddHealthAnimalDetail'),
	path('title_delete/', login_required(DeleteHealth.as_view()), name = 'DeleteHealth'),



	## dashboard start

	path('dashboard/', login_required(DashBoardView.as_view()), name = 'DashBoardView'),
	path('milk_record/', login_required(AllMilkRecord.as_view()), name = 'AllMilkRecord')






]