from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,"Adminside/index.html")


def add_category(request):
    if request.method=="POST":
        category_name = request.POST["categoryname"]
        category_image = request.FILES["categoryimage"]

        c = Category()
        c.category_name = category_name
        c.category_image = category_image
        c.save()

        return redirect(show_categories)
    else:
        return render(request,"Adminside/add_category.html")

def show_categories(request):
    categories_data = Category.objects.all()
    return render(request,"Adminside/show_categories.html",{"categories_data":categories_data})

def delete_category(request,pk):
    selected_category = Category.objects.get(id=pk)
    selected_category.delete()
    return redirect(show_categories)

def update_category(request,pk):
    selected_category = Category.objects.get(id=pk)
    if request.method=="POST":
        category_name = request.POST["categoryname"]
        category_image = request.POST["categoryimage"]

        selected_category.category_name = category_name
        selected_category.category_image = category_image
        selected_category.save()

        return redirect(show_categories)
    else:
        return render(request,"Adminside/update_category.html",{"selected_category":selected_category})

def add_product(request):
    if request.method=="POST":
        category_Id = request.POST["categoryId"]

        product_name = request.POST["productname"]
        product_description = request.POST["productdescription"]
        product_price= request.POST["productprice"]
        product_image = request.FILES["productimage"]
        isTrendingOrJustArrived = request.POST["membershipRadios"]

        p = Product()
        p.category_id = Category.objects.get(id=category_Id)
        p.product_name = product_name
        p.product_description = product_description
        p.product_price = product_price
        p.product_image = product_image
        p.is_teends_or_just_arived = isTrendingOrJustArrived
        p.save()

        return redirect(show_products)
    else:
         all_categories = Category.objects.all()
         return render(request,"Adminside/add_product.html", {"all_categories": all_categories})


def show_products(request):
    all_products = Product.objects.all()
    return render(request,"Adminside/show_products.html",{"all_products":all_products})

def delete_product(request,pk):
    selected_product = Product.objects.get(id=pk)
    selected_product.delete()
    return redirect(show_categories)

def update_product(request,pk):
    all_categories = Category.objects.all()
    selected_product = Product.objects.get(id=pk)
    if request.method=="POST":
        product_name = request.POST["productname"]
        product_description = request.POST["productdescription"]
        product_price = request.POST["productprice"]
        product_image = request.FILES["productimage"]
        isTrendingOrJustArrived = request.POST["membershipRadios"]

        selected_product.product_name = product_name
        selected_product.product_description = product_description
        selected_product.product_price = product_price
        selected_product.product_image = product_image
        selected_product.is_teends_or_just_arived = isTrendingOrJustArrived
        
        selected_product.save()

        return redirect(show_products)
    else:
        return render(request,"Adminside/update_product.html",{"selected_product":selected_product,"all_categories":all_categories})


