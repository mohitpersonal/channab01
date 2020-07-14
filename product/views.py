from django.shortcuts import render
from django.views.generic import View
from .models import Product,Category,MarketAddByAdmin,CommentReviewsStar
import sys, geocoder,json
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.


class LandingPageOfSite(View):

	'''Demonstrate docstring for confirming that this class based view will display landing page of our site'''

	def get(self,request):
		try:
			all_products = Product.objects.all().order_by('-id')
			categorylist = Category.objects.all().order_by('-id')
			all_top_product = Product.objects.filter(id__gte =1)
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
			all_lat_lang = geocoder.ip('me')
			all_markets = MarketAddByAdmin.objects.filter(is_active = True)
			city =  all_lat_lang.city
			return render(request,'product/product_add.html',locals())
		

		except Exception as e:
			print(e)
			return render(request,'product/product_add.html',locals())


	def post(self,request):
		try:
			name = request.POST.get('name')
			description = request.POST.get('description')
			price = request.POST.get('price')
			city = request.POST.get('city')
			mobilenumber = request.POST.get('mobilenumber')
			category = self.request.POST.get('category')
			marketplace = self.request.POST.get('marketplace')
			animal_type = self.request.POST.get('animal_type')
			age_of_animal = self.request.POST.get('age')
			market_instance = MarketAddByAdmin.objects.get(market_name = marketplace)

			image = request.FILES.get('main_image')
			Product.objects.create(name = name, description=description, price=price, city=city,market_instance = market_instance,category = category,  image = image, mobilenumber=mobilenumber, animal_type = animal_type, age_of_animal = age_of_animal)
			message = 'An animal has been successfully registered for sale purpose.'
			return render(request,'product/product_add.html',locals())
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
				all_products = Product.objects.filter(category = get_category)
				
				return render(request,'product/all_products.html',locals())

		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			return render(request,'product/all_products.html',locals())






class ProductDetailPage(View):

	"""Demonstrate docstring for showing that this view based function will used for filtering by category wise on main page """

	def get(self,request):
		try:
			context = {}
			id_of_product = self.request.GET.get('id')
			product_record = Product.objects.get(id = int(id_of_product))
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
				all_products = Product.objects.filter(Q(age_of_animal__lte = one_to_two_year_value))
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
				market_added = MarketAddByAdmin.objects.get(id = int(market_post))
				all_products = Product.objects.filter(market_instance = market_added)


			all_markets = MarketAddByAdmin.objects.filter(is_active = True)

			
			return render(request,'product/all_products.html',locals())

		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			return render(request,'product/all_products.html',locals())


	def get(self,request):
		try:
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
			post_id = loads_json.get('post_id')
			product_instance = Product.objects.get(id = int(post_id))
			CommentReviewsStar.objects.create(comment_on_post = comment_text, product_instance = product_instance,stars_counting = int(star_count))
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

			all_products = Product.objects.filter(market_instance = market_get)
			return render(request,'product/all_products.html',locals())

		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			return render(request,'product/all_products.html',locals())
