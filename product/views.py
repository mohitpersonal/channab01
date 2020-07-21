from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Product,PriceFilter,Category,MarketAddByAdmin,CommentReviewsStar,ProductMarket, ProductImage
import sys,json,requests
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.


class LandingPageOfSite(View):

	'''Demonstrate docstring for confirming that this class based view will display landing page of our site'''

	def get(self,request):
		try:
			all_products = Product.objects.all().order_by('-id')
			categorylist = Category.objects.all().order_by('-id')
			all_top_product_list = []

			for product_record in all_products:
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

			return render(request,'product/landing_page.html',locals())
			
		except Exception as e:
			print(sys.exc_info())
			exception_msg = 'Something went wrong,Please try again later'
			return render(request,'product/landing_page.html',locals())




class ProductList(View):

	''' Demonstrate docstring for listing all product on listing page '''


	def get(self,request):

		try:
			price_filtering = PriceFilter.objects.filter(is_active = True)
			all_category = Category.objects.values_list('category_name', flat = True)
			all_products = Product.objects.all().order_by('-id')
			all_markets = MarketAddByAdmin.objects.filter(is_active = True)
			return render(request,'product/all_products.html',locals())
		
		except Exception as e:
			print(e)
			return render(request,'product/all_products.html',locals())



class ProductAdd(View):

	''' Demonstrate docstring for add an product with category by any user'''


	def get(self,request):

		try:
			all_markets = MarketAddByAdmin.objects.filter(is_active = True)
			location_api ="http://api.ipstack.com/check?access_key={}".format(settings.GEO_API_KEY)
			geo_req = requests.get(location_api)
			geo_json = json.loads(geo_req.text)
			city = geo_json['city']
			all_category = Category.objects.values_list('category_name', flat = True)
			return render(request,'product/product_add.html',locals())
		

		except Exception as e:
			print(e)
			return render(request,'product/product_add.html',locals())


	def post(self,request):
		try:
			print(request.POST)
			name = request.POST.get('name')
			description = request.POST.get('description')
			price = request.POST.get('price')
			city = request.POST.get('city')
			mobilenumber = request.POST.get('mobilenumber')
			category = self.request.POST.get('category')
			marketplace = self.request.POST.getlist('marketplace[]')
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



			for one_market in marketplace:
				market_instance = MarketAddByAdmin.objects.get(id = int(one_market))

				ProductMarket.objects.create(market_instance = market_instance,product_instance = product_obj)


			message = 'An animal has been successfully registered for sale purpose.'
			return redirect('/product_list/')
		except:
			print(sys.exc_info())
			error = 'Something went wrong, Please try again later'
			return render(request,'product/product_add.html',locals())





class CategoryWiseSearch(View):

	"""Demonstrate docstring for showing that this view based function will used for filtering by category wise on main page """

	def get(self,request):
		try:
			context = {}
			if self.request.method == 'GET':
				get_category = self.request.GET.get('cat_id_fil')
				category_instance = Category.objects.get(category_name = get_category)
				all_products = Product.objects.filter(category_instance = category_instance)
				
				return render(request,'product/all_products.html',locals())

		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			return render(request,'product/all_products.html',locals())






class ProductDetailPage(View):

	"""Demonstrate docstring for showing that this view based function will used for filtering by category wise on main page """

	def get(self,request):
		try:
			



			#######
			id_of_product = self.request.GET.get('id')



			product_record = Product.objects.get(id = int(id_of_product))


			five_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 5).count()
			four_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 4).count()
			three_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 3).count()
			two_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 2).count()
			one_star_person = CommentReviewsStar.objects.filter(product_instance = product_record,stars_counting = 1).count()


			multiply_with_stars = (5*int(five_star_person) + 4*int(four_star_person) + 3*int(three_star_person) + 2*int(two_star_person) + 1*int(one_star_person))
			count_of_peoples = int(five_star_person) + int(four_star_person) + int(three_star_person) + int(two_star_person) + int(one_star_person)
			print(multiply_with_stars)
			if count_of_peoples == 0:
				average_by_divide = 'no_rat'
			else:
				average_by_divide = multiply_with_stars/count_of_peoples
				if average_by_divide:
					average_by_divide =int(average_by_divide)

			print("\n" * 3)
			print("average_by_divide is ----->", average_by_divide)



			products_other_images = ProductImage.objects.filter(product = product_record)

			rating_reviews = CommentReviewsStar.objects.filter(product_instance = product_record)
			return render(request,'product/product_detail.html',locals())

		except:
			print(sys.exc_info())
			return render(request,'product/product_detail.html',locals())



class FilterationAnimals(View):

	"""Demonstrate docstring for showing that this view based function will used for filtering the animals on listing page """

	def post(self,request):
		try:
			context = {}
			one_star = self.request.POST.get('one_star')
			if one_star:
				star_searching_obj  = CommentReviewsStar.objects.filter(stars_counting = int(1))
				all_products = []
				for one_object in star_searching_obj:
					product_instance = one_object.product_instance
					if product_instance not in all_products:
						all_products.append(product_instance)


			two_star = self.request.POST.get('two_star')
			if two_star:
				star_searching_obj  = CommentReviewsStar.objects.filter(stars_counting = int(2)).distinct()
				all_products = []
				for one_object in star_searching_obj:
					product_instance = one_object.product_instance
					if product_instance not in all_products:
						all_products.append(product_instance)


			three_star = self.request.POST.get('three_star')
			if three_star:
				star_searching_obj  = CommentReviewsStar.objects.filter(stars_counting = int(3))
				all_products = []
				for one_object in star_searching_obj:
					product_instance = one_object.product_instance
					if product_instance not in all_products:
						all_products.append(product_instance)


			four_start = self.request.POST.get('four_start')
			if four_start:
				star_searching_obj  = CommentReviewsStar.objects.filter(stars_counting = int(4))
				all_products = []
				for one_object in star_searching_obj:
					product_instance = one_object.product_instance
					if product_instance not in all_products:
						all_products.append(product_instance)

			five_star = self.request.POST.get('five_start')
			if five_star:
				star_searching_obj  = CommentReviewsStar.objects.filter(stars_counting = int(5))
				all_products = []
				for one_object in star_searching_obj:
					product_instance = one_object.product_instance
					if product_instance not in all_products:
						all_products.append(product_instance)

			##### age related searchings


			more_than_two_year = self.request.POST.get('more_than_two')

			one_to_two_year = self.request.POST.get('one_to_two')
			less_one_year = self.request.POST.get('less_one_year')
			if less_one_year:
				less_one_year_value = 1
				all_products = Product.objects.filter(Q(age_of_animal__lt = less_one_year_value))
			if one_to_two_year:
				one_to_two_year_value  = 2
				all_products = Product.objects.filter(age_of_animal__lte = one_to_two_year_value, age_of_animal__gte = 1)
			if more_than_two_year:
				more_than_two_year_val = 2
				all_products = Product.objects.filter(Q(age_of_animal__gt = more_than_two_year_val))

			######## milking based

			breader = self.request.POST.get('Breader')
			if breader:
				all_products = Product.objects.filter(Q(animal_type = breader))

			dry = self.request.POST.get('dry')
			if dry:
				all_products = Product.objects.filter(Q(animal_type = dry))

			milking = self.request.POST.get('Milking')
			if milking:
				all_products = Product.objects.filter(Q(animal_type = milking))



			#### market searching
			market_post = self.request.POST.get('market_added')
			if market_post:
				all_products = []
				market_added = MarketAddByAdmin.objects.get(id = int(market_post))
				product_market = ProductMarket.objects.filter(market_instance = market_added)
				for one in product_market:
					if one.product_instance not in all_products:
						all_products.append(one.product_instance)


			price_fift = self.request.POST.get('price_fift[]')

			

			if price_fift:
				split_into_list = price_fift.split()
				min_val = split_into_list[0]
				max_val = split_into_list[1]
				print("min max is ------>", min_val)
				print(max_val)


				all_products = Product.objects.filter(price__gte = int(min_val), price__lte = int(max_val))

			category_search = self.request.POST.get('category')
			if category_search:
				get_obj = Category.objects.get(category_name = category_search)
				all_products = Product.objects.filter(category_instance = get_obj)



			all_markets = MarketAddByAdmin.objects.filter(is_active = True)
			price_filtering = PriceFilter.objects.filter(is_active = True)
			all_category = Category.objects.values_list('category_name', flat = True)

			
			return render(request,'product/all_products.html',locals())

		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			return render(request,'product/all_products.html',locals())


	def get(self,request):
		try:
			all_category = Category.objects.values_list('category_name', flat = True)
			price_filtering = PriceFilter.objects.filter(is_active = True)
			all_markets = MarketAddByAdmin.objects.filter(is_active = True)
			all_products = Product.objects.all().order_by('-id')
			return render(request,'product/all_products.html',locals())

		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			return render(request,'product/all_products.html',locals())




class CommentReviewsView(View):

	"""Demonstrate docstring for showing that this view based function will used storing comment added by user"""

	def post(self,request):
		context = {}
		try:
			loads_json = json.loads(request.POST.get('type_dict'))
			comment_text = loads_json.get('text_area').strip().lower()
			star_count = loads_json.get('star_count')
			mobile_number = loads_json.get('mobile_number')
			name = loads_json.get('name')
			post_id = loads_json.get('post_id')
			product_instance = Product.objects.get(id = int(post_id))
			CommentReviewsStar.objects.create(comment_on_post = comment_text, product_instance = product_instance,mobile_number = mobile_number,name = name,stars_counting = int(star_count))
			context['status'] = 'success'
			context['save_comment'] = 'comment save'
			return HttpResponse(json.dumps(context))
		except :
			context['status'] = 'fail'
			return HttpResponse(json.dumps(context))





class MarketDetails(View):

	"""Demonstrate docstring for showing that this view based function will used for filtering an market wise product from database """

	def get(self,request):
		try:
			context = {}
			market_id = self.request.GET.get('market_based_id')
			market_get = MarketAddByAdmin.objects.get(id = int(market_id))

			product_market = ProductMarket.objects.filter(market_instance = market_get)
			all_products = []
			for one in product_market:
				if one.product_instance not in all_products:
					all_products.append(one.product_instance)

			
			return render(request,'product/all_products.html',locals())

		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			return render(request,'product/all_products.html',locals())




class AllMandies(View):

	"""Demonstrate docstring for showing that this view based function will used for filtering an market  """

	def get(self,request):

		try:
			all_markets = MarketAddByAdmin.objects.filter(is_active = True)
			return render(request,'product/all_market.html',locals())
		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			return render(request,'product/all_market.html',locals())



