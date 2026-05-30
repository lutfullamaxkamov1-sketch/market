from django.urls import path
from .views import *

urlpatterns = [
    path('base/', base, name='base'),
    path('', home, name='home'),
    path('bos/', bos, name='bos'),
    path('kirish/', Kirish, name='Kirish'),
    path('logout/', chiqish, name='logout'),
    path('Kelin_liboslari/', Kelin_liboslari, name='Kelin_liboslari'),
    path('category/<int:id>/', category_products, name='category_products'),
]