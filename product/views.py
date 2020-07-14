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
				print(get_category)
				print(all_products, type(get_category))
				
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
			print(self.request.POST)
			one_star = self.request.POST.get('one_star')
			two_star = self.request.POST.get('two_star')
			three_star = self.request.POST.get('three_star')

			four_start = self.request.POST.get('four_start')
			five_start = self.request.POST.get('five_start')
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

			breader = self.request.POST.get('Breader')
			if breader:
				all_products = Product.objects.filter(Q(animal_type = breader))

			dry = self.request.POST.get('dry')
			if dry:
				all_products = Product.objects.filter(Q(animal_type = dry))

			milking = self.request.POST.get('Milking')
			if milking:
				all_products = Product.objects.filter(Q(animal_type = milking))
			
			print(all_products)

			# all_products = Product.objects.filter()
			return render(request,'product/all_products.html',locals())

		except:
			print(sys.exc_info())
			context['status'] = 'fail'
			return render(request,'product/all_products.html',locals())


	def get(self,request):
		try:
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
			comment_text = self.request.POST.get('comment')
			print("\n" * 4)
			print("request data is --------->", request.POST)
			print("\n" * 4)
			stars1 = self.request.POST.get('star')
			stars2 = self.request.POST.get('star2')
			stars3 = self.request.POST.get('star3')
			stars4 = self.request.POST.get('star4')
			stars5 = self.request.POST.get('star5')
			stars_total = 0
			if stars1:
				stars_total = stars_total + 1
			if stars2:
				stars_total = stars_total + 1
			if stars3:
				stars_total = stars_total + 1
			if stars4:
				stars_total = stars_total + 1
			if stars5:
				stars_total = stars_total + 1


			post_id = self.request.POST.get('post_id')
			product_instance = Product.objects.get(id = int(post_id))

			CommentReviewsStar.objects.create(comment_on_post = comment_text, product_instance = product_instance,stars_counting = int(stars))
			context['status'] = 'success'
			return HttpResponse(json.dumps(context))
		except :
			context['status'] = 'fail'
			return HttpResponse(json.dumps(context))



