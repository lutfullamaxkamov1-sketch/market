from django.contrib import admin
from .models import Category, Product, WeddingCategory, WeddingProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(WeddingCategory)
admin.site.register(WeddingProduct)