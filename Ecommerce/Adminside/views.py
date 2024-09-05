from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def register(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]

        new_user = User.objects.create_user(username=username,email=email,password=password)
        new_user.first_name = firstname
        new_user.last_name = lastname
        new_user.save()

        messages.success(request,"New user register successfully.")
        return redirect(admin_login)
    else:
        return render(request,"AdminSide/register.html")

@login_required(login_url="login")
def admin_logout(request):
    logout(request)
    messages.success(request,"Logout Successfully.")
    return redirect(admin_login)
 

def admin_login(request):
    if request.method == "POST":
        userName = request.POST["username"]
        passWord = request.POST["password"]
        
        user = authenticate(username=userName,password=passWord)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully.")
            return redirect(admin_index)
        else:
            messages.warning(request,"Wrong username or password.")
            return redirect(admin_login)
    else:
        return render(request,"AdminSide/login.html")

def admin_index(request):
    return render(request,"Adminside/index.html")

def add_category(request):
    if request.method=="POST":
        if request.POST.get('num')=="":
            return render(request,"add_category.html",{'error':True})

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

def update_category(request, pk):
    selected_category = Category.objects.get(id=pk)
    if request.method == "POST":
        category_name = request.POST["categoryname"]

        if 'categoryimage' in request.FILES:
            category_image = request.FILES["categoryimage"]
            selected_category.category_image = category_image

        selected_category.category_name = category_name
        selected_category.save()

        return redirect(show_categories)
    else:
        return render(request, "Adminside/update_category.html", {"selected_category": selected_category})

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

def customer_queries(request):
    customer_queries = ContactUs.objects.all()
    return render(request,"Adminside/customer_queries.html",{"customer_queries":customer_queries})


def admin_reply_customer_queries(request,pk):
    selected_query = ContactUs.objects.get(id=pk)
    print("selected query:-", selected_query)
    if request.method == "POST":
        subject = selected_query.subject
        message = selected_query.message
        reply = request.POST.get("reply")

        email_from = settings.EMAIL_HOST_USER
        recipint_list = [selected_query.email, ]

        txt = "Message:- {m} \n Reply:- {r}".format(m=message,r=reply)
        send_mail( subject,txt, email_from, recipint_list )
    
        selected_query.reply = reply
        selected_query.is_replied = True
        selected_query.save()

        print("subject:-",subject, "message :-", message, "reply:-", reply) 
        messages.success(request,"Customer Queries Replied Successfully.")
        return redirect(customer_queries)
    else:
        return render(request,"Adminside/admin_reply_customer_queries.html",{"selected_query":selected_query})    

def add_banner(request):
    if request.method=="POST":
        
        banner_image = request.FILES["bannerimage"]
        isYesOrNo = request.POST["membershipRadios"]

        b = AddBanner()
        b.banner_image = banner_image
        b.is_show = isYesOrNo
        print("is_Yes_Or_No:-",isYesOrNo)
        b.save()

        return redirect(show_banner)
    else:
        return render(request,"Adminside/add_banner.html",)

def show_banner(request):
    banner_data = AddBanner.objects.all()
    print("banner data:-", len(banner_data))
    return render(request,"Adminside/show_banner.html",{"banner_data":banner_data})        

def update_banner(request, pk):
    selected_banner = AddBanner.objects.get(id=pk)
    if request.method == "POST":
     
        if 'bannerimage' in request.FILES:
            banner_image = request.FILES["bannerimage"]
            isYesOrNo = request.POST["membershipRadios"]

            selected_banner.banner_image = banner_image
            selected_banner.is_show = isYesOrNo
            print("is_Yes_Or_No:-",isYesOrNo)

            selected_banner.save()
        
        return redirect(show_banner)
    else:
        return render(request, "Adminside/update_banner.html", {"selected_banner": selected_banner})
    

def delete_banner(request,pk):
    selected_banner = AddBanner.objects.get(id=pk)
    selected_banner.delete()
    return redirect(show_banner)

def add_offer(request):
    if request.method=="POST":
        
        offer_image = request.FILES["offerimage"]
        offer_description = request.POST["offerdescription"]
        offer_title = request.POST["offertitle"]
        isYesOrNo = request.POST["membershipRadios"]

        o = AddOffers()
        o.offer_image = offer_image
        o.offer_description = offer_description
        o.offer_title = offer_title
        o.is_showing = isYesOrNo
        print("is_Yes_Or_No:-",isYesOrNo)
        o.save()

        return redirect(show_offer)
    else:
        return render(request,"Adminside/add_offer.html",)

def show_offer(request):
    offer_data = AddOffers.objects.all()
    print("offer data:-", len(offer_data))
    return render(request,"Adminside/show_offer.html",{"offer_data":offer_data})        


def update_offer(request, pk):
    selected_offer = AddOffers.objects.get(id=pk)
    if request.method == "POST":
     
        if 'offerimage' in request.FILES:
            
            offer_image = request.FILES["offerimage"]
            offer_description = request.POST["offerdescription"]
            offer_title = request.POST["offertitle"]
            isYesOrNo = request.POST["membershipRadios"]

            selected_offer.offer_image = offer_image
            selected_offer.offer_description = offer_description
            selected_offer.offer_title = offer_title
            selected_offer.is_showing = isYesOrNo
            print("is_Yes_Or_No:-",isYesOrNo)

            selected_offer.save()
        
        return redirect(show_offer)
    else:
        return render(request, "Adminside/update_offer.html", {"selected_offer": selected_offer})


def delete_offer(request,pk):
    selected_offer = AddOffers.objects.get(id=pk)
    selected_offer.delete()
    return redirect(show_offer)

