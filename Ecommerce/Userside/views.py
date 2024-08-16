from django.shortcuts import render, redirect
from django.http import HttpResponse
from Adminside.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages




# Create your views here.
def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('passwd')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        phonenumber = request.POST.get('phonenumber')
        user_image = request.POST.get('userimage')
        pincode  = request.POST.get('pincode')
        locality = request.POST.get('locality')
        landmark = request.POST.get('landmark') 

        print("User details:- ", username, password, email, firstname, lastname)
        print("Other details:- ", phonenumber, user_image,pincode,locality,landmark)

        
        n_user = User.objects.create_user(username=username, email=email, password=password)
        n_user.first_name = firstname
        n_user.last_name = lastname
        n_user.save()
        print("Created user id:-",User.objects.get(id=n_user.id))
        
        
        c_user = UserProfile()
        c_user.userId = User.objects.get(id=n_user.id)
        c_user.user_image = user_image
        c_user.phone_number = phonenumber
        c_user.address = address
        c_user.pincode = pincode
        c_user.locality = locality
        c_user.save()
        
        return redirect(user_login)
    else:
        return render(request,"Userside/user_register.html")

def user_login(request):
    if request.method == "POST":
        userName = request.POST["username"]
        passWord = request.POST["password"]
        
        user = authenticate(username=userName,password=passWord)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully.")
            return redirect(user_dashboard)
        else:
            messages.warning(request,"Wrong username or password.")
            return redirect(user_login)
    else:
        return render(request,"Userside/user_login.html")


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

def user_logout(request):
    logout(request)
    messages.success(request,"Logout Successfully.")
    return redirect(user_dashboard)

def category_based_products(request,pk):
    categories_data = Category.objects.all()[:6]
    filtered_products_according_category = Product.objects.filter(category_id = Category.objects.get(id=pk))
    print("Filtered products according to the category :- ", filtered_products_according_category)
    return render(request,"Userside/category_based_products.html",{"categories_data":categories_data,"filtered_products_according_category":filtered_products_according_category})

def view_all_products(request):
    categories_data = Category.objects.all()[:6]
    all_products = Product.objects.all()
    return render(request,"Userside/view_all_products.html",{"categories_data":categories_data,"all_products":all_products,})

def all_categories(request):
    categories_data = Category.objects.all()[:6]
    all_categories = Category.objects.all()
    return render(request,"Userside/all_categories.html",{"categories_data":categories_data,"all_categories":all_categories})

def product_details(request,pk):
    categories_data = Category.objects.all()[:10]
    product_details = Product.objects.get(id=pk)
    print("Product Details :- ", product_details)
    return render(request,"Userside/product_details.html",{"categories_data":categories_data,"product_details":product_details})
    