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
				context['error'] = 'Bad Request,Token Not Found!'
				context['status'] = 500
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


			product_obj = Product.objects.create(name = name, description=description, price=price, city=city,category_instance = category_instance,  image = image, mobilenumber=mobilenumber, animal_type = animal_type, age_of_animal = age_of_animal)
			ist_image = request.FILES.get('ist_image')
			sec_image = request.FILES.get('sec_image')
			iiird_image = request.FILES.get('iiird_image')
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
			context['error'] = 'Something went wrong, Please try again later'
			context['status'] = 500
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
				context['error'] = 'Bad Request,Token Not Found!'
				context['status'] = 500
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

			context['all_market_list'] = all_market_list
			context['all_market_list'] = top_10_product
			context['status'] = 200
			return HttpResponse(json.dumps(context))

			
		except Exception as e:
			context = {}
			print(sys.exc_info())
			context['error'] = 'Something went wrong, Please try again later'
			context['status'] = 500
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
				context['error'] = 'Bad Request,Token Not Found!'
				context['status'] = 500
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
			top_10_product = []
			for one_top in all_products:
				top_product_dict = {}
				top_product_dict['product_category_name'] = one_top.category_instance.category_name
				top_product_dict['id_of_product'] = one_top.id
				top_product_dict['product_name'] = one_top.name
				top_product_dict['product_price'] = str(one_top.price)
				top_product_dict['seller_mobilenumber'] = one_top.mobilenumber
				top_product_dict['seller_city'] = one_top.city
				top_product_dict['product_main_image'] = str(one_top.image)
				top_10_product.append(top_product_dict)


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


			context['status'] = 200
			context['all_market_list'] = all_market_list
			context['top_10_product'] = top_10_product
			context['all_category_list'] = all_category_list
			context['price_filtering_list'] = price_filtering_list
			return HttpResponse(json.dumps(context))
			
		
		except Exception as e:
			print(e)
			context = {}
			print(sys.exc_info())
			context['error'] = 'Something went wrong, Please try again later'
			context['status'] = 500
			return HttpResponse(json.dumps(context))
			


