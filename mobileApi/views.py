from django.http import HttpResponse
from product.models import Product,PriceFilter,Category,MarketAddByAdmin,CommentReviewsStar,ProductMarket, ProductImage
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
import ast,sys,json
from rest_framework.authtoken.models import Token
from django.conf import settings


class ProductPageApi(APIView):

	''' Demonstrate docstring for add an product with category by any user'''

	parser_classes = (MultiPartParser, FormParser)


	def post(self,request,*args, **kwargs):
		try:
			api_key = settings.API_KEY_FOR_SECURITY
			print(request.META.get('HTTP_X_API_KEY'))
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context = {}
				print(sys.exc_info())
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))

			name = request.POST.get('name')
			description = request.POST.get('description')
			price = request.POST.get('price')
			city = request.POST.get('city')
			mobilenumber = request.POST.get('mobilenumber')
			category = self.request.POST.get('category')
			marketplace = self.request.POST.get('marketplace[]')
			print(marketplace)
			animal_type = self.request.POST.get('animal_type')
			age_of_animal = self.request.POST.get('age')
			category_instance = Category.objects.get(category_name = category)

			image = request.FILES.get('main_image')

			if not name:
				context = {}
				context['message'] = 'Please Fill out Your Animal Name'
				context['status'] = 200
				return HttpResponse(json.dumps(context))

			if not price:
				context = {}
				context['message'] = 'Please Fill out Price of your animal'
				context['status'] = 200
				return HttpResponse(json.dumps(context))

			if not mobilenumber:
				context = {}
				context['message'] = 'Please Fill out Your Mobile Number'
				context['status'] = 200
				return HttpResponse(json.dumps(context))

			if not category:
				context = {}
				context['message'] = 'Please Fill out Category of Animal'
				context['status'] = 200
				return HttpResponse(json.dumps(context))

			if not image:
				context = {}
				context['message'] = 'Please Fill out Main Image of your animal'
				context['status'] = 200
				return HttpResponse(json.dumps(context))



			product_obj = Product.objects.create(name = name, description=description, price=price, city=city,category_instance = category_instance,  image = image, mobilenumber=mobilenumber, animal_type = animal_type, age_of_animal = age_of_animal)
			ist_image = request.FILES.get('ist_image')
			sec_image = request.FILES.get('sec_image')
			iiird_image = request.FILES.get('third_image')
			fourth_image = request.FILES.get('fourth_image')
			fifth_image = request.FILES.get('fifth_image')
			if ist_image:
				ProductImage.objects.create(product = product_obj,image = ist_image)
			if sec_image:
				ProductImage.objects.create(product = product_obj,image = sec_image)
			if iiird_image:
				ProductImage.objects.create(product = product_obj,image = iiird_image)
			if fourth_image:
				ProductImage.objects.create(product = product_obj,image = fourth_image)
			if fifth_image:
				ProductImage.objects.create(product = product_obj,image = fifth_image)

			x = ast.literal_eval(marketplace)
			make_list = [n.strip() for n in x]

			for one_market in make_list:
				market_instance = MarketAddByAdmin.objects.get(id = int(one_market))

				ProductMarket.objects.create(market_instance = market_instance,product_instance = product_obj)

			context = {}
			context['message'] = 'An animal has been successfully registered for sale purpose.'
			context['status'] = 200
			return HttpResponse(json.dumps(context))
		except:
			context = {}
			print(sys.exc_info())
			context['status'] = 500
			context['message'] = 'Something went wrong,Please try again later'

			return HttpResponse(json.dumps(context))


class HomePageApi(APIView):
	def get(self,request):
		context = {}

		try:
			api_key = settings.API_KEY_FOR_SECURITY
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context = {}
				print(sys.exc_info())
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))
			all_product = Product.objects.all().order_by('-id')
			categorylist = Category.objects.all().order_by('-id')
			all_top_product_list = []
			for product_record in all_product:
				five_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 5).count()
				four_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 4).count()
				three_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 3).count()
				two_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 2).count()
				one_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 1).count()

				multiply_with_stars = (5*int(five_star_person) + 4*int(four_star_person) + 3*int(three_star_person) + 2*int(two_star_person) + 1*int(one_star_person))

				count_of_peoples = int(five_star_person) + int(four_star_person) + int(three_star_person) + int(two_star_person) + int(one_star_person)
				if not count_of_peoples == 0:
					average_by_divide = multiply_with_stars/count_of_peoples
					if average_by_divide > 4 :
						if len(all_top_product_list) < 10:
							all_top_product_list.append(product_record)
							
						else:
							break
					elif average_by_divide >= 3 :
						if len(all_top_product_list) < 10:
							all_top_product_list.append(product_record)
						else:
							break
			all_markets = MarketAddByAdmin.objects.filter(is_active = True)
			all_market_list = []

			for one_market in all_markets:
				market_dict = {}
				market_dict['market_name'] = one_market.market_name
				date = one_market.date
				str_date = date.strftime("%d-%m-%Y %H:%M:%S")
				market_dict['date'] = str_date
				market_dict['description'] = one_market.description
				market_dict['is_active'] = one_market.is_active
				market_dict['location'] = one_market.location
				market_dict['market_image'] = str(one_market.market_image)
				all_market_list.append(market_dict)

			top_10_product = []

			for one_top in all_top_product_list:
				top_product_dict = {}
				top_product_dict['product_category_name'] = one_top.category_instance.category_name
				top_product_dict['id_of_product'] = one_top.id
				top_product_dict['product_name'] = one_top.name
				top_product_dict['product_price'] = str(one_top.price)
				top_product_dict['seller_mobilenumber'] = one_top.mobilenumber
				top_product_dict['seller_city'] = one_top.city
				top_product_dict['product_main_image'] = str(one_top.image)
				top_10_product.append(top_product_dict)

			category_list = []

			for one_category in categorylist:
				category_dict = {}
				category_dict['name_of_category'] = one_category.category_name
				category_dict['id'] = one_category.id
				category_dict['image'] = str(one_category.image)
				category_dict['description'] = one_category.description
				category_list.append(category_dict)






			context['cattle_market_list'] = all_market_list
			context['top_10_product'] = top_10_product
			context['all_categories'] = category_list
			context['message'] = 'Data Found'
			context['status'] = 200
			return HttpResponse(json.dumps(context))

			
		except Exception as e:
			context = {}
			print(sys.exc_info())
			context['status'] = 500
			context['message'] = 'Something went wrong,Please try again later'
			return HttpResponse(json.dumps(context))
			














class MobileProductListApi(APIView):

	''' Demonstrate docstring for listing all product on listing page '''


	def get(self,request):

		try:
			context = {}
			api_key = settings.API_KEY_FOR_SECURITY
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context = {}
				print(sys.exc_info())
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))


			price_filtering = PriceFilter.objects.filter(is_active = True)
			price_filtering_list = []
			for one_price in price_filtering:
				price_dict = {}
				price_dict['min_val'] = one_price.min_val
				price_dict['max_val'] = one_price.max_val
				price_filtering_list.append(price_dict)



			all_category = Category.objects.values_list('category_name', flat = True)
			all_category_list = []
			for one_category in all_category:
				category_dict = {}
				category_dict['category_name'] = one_category
				all_category_list.append(category_dict)






			all_products = Product.objects.all().order_by('-id')
			all_products_list = []
			for one_top in all_products:
				top_product_dict = {}
				top_product_dict['product_category_name'] = one_top.category_instance.category_name
				top_product_dict['id_of_product'] = one_top.id
				top_product_dict['product_name'] = one_top.name
				top_product_dict['product_price'] = str(one_top.price)
				top_product_dict['seller_mobilenumber'] = one_top.mobilenumber
				top_product_dict['seller_city'] = one_top.city
				top_product_dict['product_main_image'] = str(one_top.image)
				all_products_list.append(top_product_dict)


			all_markets = MarketAddByAdmin.objects.filter(is_active = True)

			all_market_list = []
			for one_market in all_markets:
				market_dict = {}
				market_dict['market_name'] = one_market.market_name
				date = one_market.date
				str_date = date.strftime("%d-%m-%Y %H:%M:%S")
				market_dict['date'] = str_date
				market_dict['description'] = one_market.description
				market_dict['is_active'] = one_market.is_active
				market_dict['location'] = one_market.location
				market_dict['market_image'] = str(one_market.market_image)
				all_market_list.append(market_dict)


			context['message'] = 'Data Found'
			context['status'] = 200
			context['all_market_list'] = all_market_list
			context['all_products_list'] = all_products_list
			context['all_category_list'] = all_category_list
			context['price_filtering_list'] = price_filtering_list
			return HttpResponse(json.dumps(context))
			
		
		except Exception as e:
			print(e)
			context = {}
			context['status'] = 500
			context['message'] = 'Something went wrong,Please try again later'
			return HttpResponse(json.dumps(context))
			



class MobileApiCategoryWiseSearch(APIView):

	"""Demonstrate docstring for showing that this view based function will used for filtering by category wise on main page """

	def get(self,request):
		try:
			context = {}
			api_key = settings.API_KEY_FOR_SECURITY
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context = {}
				print(sys.exc_info())
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))

			get_category = self.request.GET.get('cat_id_fil')
			category_instance = Category.objects.get(category_name = get_category)
			all_products = Product.objects.filter(category_instance = category_instance)
			all_products_list = []

			for one_top in all_products:
				top_product_dict = {}
				top_product_dict['product_category_name'] = one_top.category_instance.category_name
				top_product_dict['id_of_product'] = one_top.id
				top_product_dict['product_name'] = one_top.name
				top_product_dict['product_price'] = str(one_top.price)
				top_product_dict['seller_mobilenumber'] = one_top.mobilenumber
				top_product_dict['seller_city'] = one_top.city
				top_product_dict['product_main_image'] = str(one_top.image)
				all_products_list.append(top_product_dict)

			context['message'] = 'Data Found'
			context['status'] = 200
			context['category_name'] = category_instance.category_name
			context['all_products_list'] = all_products_list
			return HttpResponse(json.dumps(context))
			
			

		except Exception as e:
			print(e)
			context = {}
			print(sys.exc_info())
			context['status'] = 500
			context['message'] = 'Something went wrong,Please try again later'
			return HttpResponse(json.dumps(context))
			







class MobileProductDetailPage(APIView):

	"""Demonstrate docstring for showing that this api view based function will used for show all details of product on detail page """

	def get(self,request):
		try:
			#######
			context = {}
			api_key = settings.API_KEY_FOR_SECURITY
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context = {}
				print(sys.exc_info())
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))

			id_of_product = self.request.GET.get('id')



			product_record = Product.objects.get(id = int(id_of_product))


			five_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 5).count()
			four_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 4).count()
			three_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 3).count()
			two_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 2).count()
			one_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 1).count()


			multiply_with_stars = (5*int(five_star_person) + 4*int(four_star_person) + 3*int(three_star_person) + 2*int(two_star_person) + 1*int(one_star_person))
			count_of_peoples = int(five_star_person) + int(four_star_person) + int(three_star_person) + int(two_star_person) + int(one_star_person)
			if count_of_peoples == 0:
				average_by_divide = 'no_rat'
			else:
				average_by_divide = multiply_with_stars/count_of_peoples
				if average_by_divide:
					average_by_divide =int(average_by_divide)

			products_other_images = ProductImage.objects.filter(product = product_record)


			product_info = {}
			product_info['product_name'] = product_record.name
			product_info['price'] = str(product_record.price)
			product_info['rating_average'] = str(average_by_divide)
			product_info['city_of_product_seller'] = product_record.city
			product_info['mobilenumber'] = product_record.mobilenumber
			product_info['id_of_product'] = product_record.id
			product_info['description_product'] = product_record.description



			list_of_images = []
			for one_image in products_other_images:
				images_dict = []
				images_dict['image'] = one_image.image
				list_of_images.append(images_dict)


			rating_reviews = CommentReviewsStar.objects.filter(product_instance = product_record)
			all_rates_and_comments = []


			for one_rate in rating_reviews:
				rate_dict = {}
				rate_dict['stars_counting'] = one_rate.stars_counting
				rate_dict['comment_on_post'] = one_rate.comment_on_post
				rate_dict['name_of_commenter'] = one_rate.name
				created_on = one_rate.created_on
				make_str = created_on.strftime("%d-%m-%Y %H:%I:%S")
				rate_dict['time_of_comment'] = make_str
				all_rates_and_comments.append(rate_dict)


			context['message'] = 'Data Found'
			context['status'] = 200
			context['all_rates_and_comments'] = all_rates_and_comments
			context['list_of_images'] = list_of_images
			context['product_info'] = product_info
			return HttpResponse(json.dumps(context))
			
		except:
			print(sys.exc_info())
			context = {}
			print(sys.exc_info())
			context['status'] = 500
			context['message'] = 'Something went wrong,Please try again later'
			return HttpResponse(json.dumps(context))
			

















class ApiCommentReviewsView(APIView):

	"""Demonstrate docstring for showing that this view based function will used storing comment added by user through mobile"""

	def post(self,request):
		try:
			context = {}
			api_key = settings.API_KEY_FOR_SECURITY
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context = {}
				print(sys.exc_info())
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))
			comment_text = request.POST.get('text_area').strip().lower()
			if not comment_text:
				context = {}
				context['message'] = 'Please Fill out Your Comment Text'
				context['status'] = 200
				return HttpResponse(json.dumps(context))




			star_count = request.POST.get('star_count')
			if not star_count:
				context = {}
				context['message'] = 'Please provide any rating to this product'
				context['status'] = 200
				return HttpResponse(json.dumps(context))

			mobile_number = request.POST.get('mobile_number')
			name = request.POST.get('name')
			if not name:
				context = {}
				context['message'] = 'Please Fill out your name'
				context['status'] = 200
				return HttpResponse(json.dumps(context))

			post_id = request.POST.get('post_id')
			product_instance = Product.objects.get(id = int(post_id))
			CommentReviewsStar.objects.create(comment_on_post = comment_text, product_instance = product_instance,mobile_number = mobile_number,name = name,stars_counting = int(star_count))
			context['message'] = 'Data has been saved successfully'
			context['status'] = 200
			return HttpResponse(json.dumps(context))
		except :
			context['status'] = 500
			context['message'] = 'Something went wrong,Please try again later'
			return HttpResponse(json.dumps(context))





class ApiMarketDetails(APIView):

	"""Demonstrate docstring for showing that this view based function will used for filtering an market wise product from database """

	def get(self,request):
		try:
			context = {}
			api_key = settings.API_KEY_FOR_SECURITY
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context = {}
				print(sys.exc_info())
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))
			context = {}
			market_id = self.request.GET.get('market_based_id')
			market_get = MarketAddByAdmin.objects.get(id = int(market_id))

			product_market = ProductMarket.objects.filter(market_instance = market_get)
			all_products = []
			for one in product_market:
				if one.product_instance not in all_products:
					all_products.append(one.product_instance)


			all_products_list = []

			for one_top in all_products:
				top_product_dict = {}
				top_product_dict['product_category_name'] = one_top.category_instance.category_name
				top_product_dict['id_of_product'] = one_top.id
				top_product_dict['product_name'] = one_top.name
				top_product_dict['product_price'] = str(one_top.price)
				top_product_dict['seller_mobilenumber'] = one_top.mobilenumber
				top_product_dict['seller_city'] = one_top.city
				top_product_dict['product_main_image'] = str(one_top.image)
				all_products_list.append(top_product_dict)

			context['message'] = 'Data Found'
			context['status'] = 200
			context['market_name'] = market_get.market_name
			context['all_products_list'] = all_products_list
			return HttpResponse(json.dumps(context))


		except:
			context = {}
			print(sys.exc_info())
			context['status'] = 500
			context['message'] = 'Something went wrong,Please try again later'
			return HttpResponse(json.dumps(context))
			



class AllMandiesApi(APIView):

	"""Demonstrate docstring for showing that this view based function will used for filtering an market  """

	def get(self,request):

		try:
			context = {}
			api_key = settings.API_KEY_FOR_SECURITY
			token_From_request = request.META.get('HTTP_X_API_KEY')
			if api_key != token_From_request:
				context = {}
				print(sys.exc_info())
				context['message'] = 'Bad Request,Token Not Found!'
				context['status'] = 403
				return HttpResponse(json.dumps(context))
			all_markets = MarketAddByAdmin.objects.filter(is_active = True)
			all_mandis_list = []

			for one_top in all_markets:
				top_product_dict = {}
				top_product_dict['market_id'] = one_top.id
				top_product_dict['description'] = one_top.description
				top_product_dict['market_name'] = one_top.market_name
				top_product_dict['location'] = one_top.location
				top_product_dict['market_image'] = str(one_top.market_image)
				all_mandis_list.append(top_product_dict)

			context['message'] = 'Data Found'
			context['status'] = 200
			context['all_market_list'] = all_mandis_list
			return HttpResponse(json.dumps(context))


		except:
			print(sys.exc_info())
			context['status'] = 500
			context['message'] = 'Something went wrong,Please try again later'
			return render(request,'product/all_market.html',locals())


