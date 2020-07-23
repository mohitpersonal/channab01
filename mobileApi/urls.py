from django.urls import path
from .views import *

urlpatterns = [

	### apis related to product Adding page

    path('product_add/', ProductPageApi.as_view(), name = 'ProductPageApi'),
    path('HomePageApi/', HomePageApi.as_view(),name =  'HomePageApi'),
    path('all_products/', MobileProductListApi.as_view(), name = 'MobileProductListApi'),
    path('category_wise_search/', MobileApiCategoryWiseSearch.as_view(), name = 'MobileApiCategoryWiseSearch'),
    path('product_detail_api/', MobileProductDetailPage.as_view(), name = 'MobileProductDetailPage'),
    path('market_product/', ApiMarketDetails.as_view(), name = 'ApiMarketDetails'),
    path("all_markets/", AllMandiesApi.as_view(), name = 'AllMandiesApi'),
    path("reviews_start_post/", ApiCommentReviewsView.as_view(), name = 'ApiCommentReviewsView')



]