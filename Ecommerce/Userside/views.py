from django.shortcuts import render
from django.http import HttpResponse
from Adminside.models import *


# Create your views here.
def user_register(request):
    categories_data = Category.objects.all()[:6]
    trendy_products = Product.objects.filter(is_teends_or_just_arived=True)[:8]
    just_arrive_products = Product.objects.filter(is_teends_or_just_arived=False)[:8]
    return render(request,"Userside/user_register.html",{"categories_data":categories_data,"trendy_products":trendy_products,"just_arrive_products":just_arrive_products})

def user_login(request):
    categories_data = Category.objects.all()[:6]
    trendy_products = Product.objects.filter(is_teends_or_just_arived=True)[:8]
    just_arrive_products = Product.objects.filter(is_teends_or_just_arived=False)[:8]
    return render(request,"Userside/user_login.html",{"categories_data":categories_data,"trendy_products":trendy_products,"just_arrive_products":just_arrive_products})

def index(request):
    categories_data = Category.objects.all()[:6]
    trendy_products = Product.objects.filter(is_teends_or_just_arived=True)[:8]
    just_arrive_products = Product.objects.filter(is_teends_or_just_arived=False)[:8]
    return render(request,"Userside/index.html",{"categories_data":categories_data,"trendy_products":trendy_products,"just_arrive_products":just_arrive_products})
  
def user_dashboard(request):
    categories_data = Category.objects.all()[:6]
    trendy_products = Product.objects.filter(is_teends_or_just_arived=True)[:8]
    just_arrive_products = Product.objects.filter(is_teends_or_just_arived=False)[:8]
    return render(request,"Userside/dashboard.html",{"categories_data":categories_data,"trendy_products":trendy_products,"just_arrive_products":just_arrive_products})
    
