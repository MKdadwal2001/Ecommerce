from django.shortcuts import render
from django.http import HttpResponse
from Adminside.models import *

# Create your views here.
def user_register(request):
    categories_data = Category.objects.all()
    limited_categories = Category.objects.all()[:8]
    return render(request,"Userside/user_er.htmregistl",{"categories_data":categories_data})

def user_login(request):
    categories_data = Category.objects.all()
    limited_categories = Category.objects.all()[:8]
    return render(request,"Userside/user_login.html",{"categories_data":categories_data})

def index(request):
    return render(request,"Userside/index.html")

def user_dashboard(request):
    categories_data = Category.objects.all()
    limited_categories = Category.objects.all()[:8]
    return render(request,"Userside/dashboard.html",{"categories_data":categories_data})


