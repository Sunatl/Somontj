from django.contrib import admin
from .models import Category, Product, Inquiry,CustomUser

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Inquiry)
admin.site.register(CustomUser)
