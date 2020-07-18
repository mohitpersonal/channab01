from django.contrib import admin
from .models import PriceFilter,Product,ProductMarket, Category, ProductImage,MarketAddByAdmin

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(MarketAddByAdmin)
admin.site.register(ProductMarket)
admin.site.register(PriceFilter)
