from django.urls import path
from .views import *


urlpatterns = [

	### functions related to dashoboard and product listing page

    path('', LandingPageOfSite.as_view(), name = 'LandingPageOfSite'),
    path('product_list/', ProductList.as_view(), name = 'ProductList'),
    path('product_add/', ProductAdd.as_view(), name = 'ProductAdd'),
    path('search_cat/', CategoryWiseSearch.as_view(), name = 'CategoryWiseSearch'),
    path('one_detail/', ProductDetailPage.as_view(), name = 'ProductDetailPage'),
    path('filter_data/', FilterationAnimals.as_view(), name = 'FilterationAnimals'),
    path('comment/', CommentReviewsView.as_view(), name = 'CommentReviewsView')

]