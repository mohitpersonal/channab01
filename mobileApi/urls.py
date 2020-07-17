from django.urls import path
from .views import *

urlpatterns = [

	### apis related to product Adding page

    path('', ProductPageApi.as_view(), name = 'ProductPageApi'),

]