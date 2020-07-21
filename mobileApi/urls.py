from django.urls import path
from .views import *

urlpatterns = [

	### apis related to product Adding page

    path('', ProductPageApi.as_view(), name = 'ProductPageApi'),
    path('HomePageApi/', HomePageApi.as_view(),name =  'HomePageApi'),
    path('all_products/', MobileProductListApi.as_view(), name = 'MobileProductListApi')

]