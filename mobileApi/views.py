from django.shortcuts import render,redirect
import sys
from django.views import View
# Create your views here.



class ProductPageApi(View):

	''' Demonstrate docstring for add an product with category by any user'''


	def post(self,request):
		try:
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

