from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import WeddingCategory, WeddingProduct
def base(request):
    return render(request, "base.html")


def home(request):
    return render(request, 'home.html')

def bos(request):
    return render(request, 'bos.html')

def Kirish(request):
    return render(request, 'Kirish.html')



def home(request):
    return render(request, 'home.html')


def Kirish(request):
    if request.method == "POST" and request.POST.get("type") == "login":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Login yoki parol xato")

    if request.method == "POST" and request.POST.get("type") == "register":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu foydalanuvchi mavjud")
        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )

            login(request, user)

            return redirect('home')

    return render(request, 'kirish.html')


def chiqish(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render
from .models import Product, WeddingCategory

def home(request):

    products = Product.objects.all()

    return render(request, 'home.html', {
        'products': products
    })
    
def Kelin_liboslari(request):
    return render(request, 'Kelin_liboslari.html')


def home(request):

    products = WeddingProduct.objects.all()

    categories = WeddingCategory.objects.all()

    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })
    
def category_products(request, id):

    products = WeddingProduct.objects.filter(category_id=id)

    categories = WeddingCategory.objects.all()

    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })