from django.urls import path
from .views import *
from .livestock import RegisterView,ApiLoginView,ApiLogoutView,ResetPassword,ForgetView,APiAnimalLivestock


urlpatterns = [

	### apis related to product Adding page

    path('product_add/', ProductPageApi.as_view(), name = 'ProductPageApi'),
    path('HomePageApi/', HomePageApi.as_view(),name =  'HomePageApi'),
    path('all_products/', MobileProductListApi.as_view(), name = 'MobileProductListApi'),
    path('category_wise_search/', MobileApiCategoryWiseSearch.as_view(), name = 'MobileApiCategoryWiseSearch'),
    path('product_detail_api/', MobileProductDetailPage.as_view(), name = 'MobileProductDetailPage'),
    path('market_product/', ApiMarketDetails.as_view(), name = 'ApiMarketDetails'),
    path("all_markets/", AllMandiesApi.as_view(), name = 'AllMandiesApi'),
    path("reviews_start_post/", ApiCommentReviewsView.as_view(), name = 'ApiCommentReviewsView'),
    path('filteration_api/', MobileFilterApi.as_view(), name = 'MobileFilterApi'),



    ##############live stock module api start

    path('register/', RegisterView.as_view(), name = 'RegisterView'),
    path('login/', ApiLoginView.as_view(), name = 'ApiLoginView'),
    path('logout/', ApiLogoutView.as_view(), name = 'ApiLogoutView'),
    path('forgot_password/', ForgetView.as_view(), name = 'ForgetView'),
    path('reset_password/', ResetPassword.as_view(), name = 'ResetPassword'),
    path('live_animal_Add/', APiAnimalLivestock.as_view(), name = 'APiAnimalLivestock'),
    







]