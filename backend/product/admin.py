from django.contrib import admin

from .models import Cart, CartProduct, Category, Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartProduct)
admin.site.register(Cart)
