from django.shortcuts import render
from django.http import HttpResponse
from Adminside.models import *
from django.contrib.auth.models import User


# Create your views here.
def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        phonenumber = request.POST.get('phonenumber')
        user_image = request.POST.get('userimage')
        Pincode  = request.POST.get('pincode')
        locality = request.POST.get('locality')
        landmark = request.POST.get('landmark') 

        n_user = User.objects.create_user(username=username, email=email, password=password)
        n_user.first_name = firstname
        n_user.last_name = lastname
        n_user.save()
        print(User.objects.get(id=n_user.id))
        
        
        c_user = CustomUser()
        c_user.phone_number = phonenumber
        c_user.address = address
        c_user.user_image = user_image
        c_user.pincode = Pincode
        c_user.locality = locality
        c_user.landmark = landmark
        c_user.user_id = User.objects.get(id=n_user.id)
        c_user.save()
        return HttpResponse(c_user)
    else:
        return render(request,"Userside/user_register.html")

def user_login(request):
    if request.method == "POST":
        userName = request.POST["username"]
        passWord = request.POST["password"]

        categories_data = Category.objects.all()[:6]
        trendy_products = Product.objects.filter(is_teends_or_just_arived=True)[:8]
        just_arrive_products = Product.objects.filter(is_teends_or_just_arived=False)[:8]
        return HttpResponse(user_login)
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

