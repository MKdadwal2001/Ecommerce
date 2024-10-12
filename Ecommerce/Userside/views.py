from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Adminside.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import string, random

def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('passwd', '')
        email = request.POST.get('email', '').strip()
        firstname = request.POST.get('firstname', '').strip()
        lastname = request.POST.get('lastname', '').strip()
        address = request.POST.get('address', '').strip()
        phonenumber = request.POST.get('phonenumber', '').strip()
        user_image = request.FILES.get('userimage') 
        pincode = request.POST.get('pincode', '').strip()
        locality = request.POST.get('locality', '').strip()
        landmark = request.POST.get('landmark', '').strip()

        if not all([username, password, email, firstname, lastname, phonenumber, pincode, locality, landmark, address]):
            messages.error(request, "Please fill in all the required fields.")
            return render(request, "Userside/user_register.html", {
                "banner_data": AddBanner.objects.filter(is_show=True),
                "categories_data": Category.objects.all()[:15]
            })

        try:
            n_user = User.objects.create_user(username=username, email=email, password=password)
            n_user.first_name = firstname
            n_user.last_name = lastname
            n_user.save()

            c_user = UserProfile()
            c_user.userId = n_user 
            c_user.user_image = user_image
            c_user.phone_number = phonenumber
            c_user.address = address
            c_user.pincode = pincode
            c_user.locality = locality
            c_user.landmark = landmark 
            c_user.save()

            return redirect('user-login') 
        except Exception as e:
            messages.error(request, "There was an error creating your account. Please try again.")
            return render(request, "Userside/user_register.html", {
                "banner_data": AddBanner.objects.filter(is_show=True),
                "categories_data": Category.objects.all()[:15]
            })

    else:
        banner_data = AddBanner.objects.filter(is_show=True)
        categories_data = Category.objects.all()[:15]
        return render(request, "Userside/user_register.html", {
            "banner_data": banner_data,
            "categories_data": categories_data
        })

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
        banner_data = AddBanner.objects.filter(is_show=True)
        categories_data = Category.objects.all()[:15]
        return render(request,"Userside/user_register.html",{"banner_data":banner_data,"categories_data":categories_data})

def user_login(request):
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]

    if request.method == "POST":
        userName = request.POST.get("username", "").strip()
        passWord = request.POST.get("password", "").strip()
        
        if not userName or not passWord:
            messages.warning(request, "Please first fill in all the details that are given on the page.")
            return render(request, "Userside/user_login.html", {"banner_data": banner_data, "categories_data": categories_data})

        user = authenticate(username=userName, password=passWord)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully.")
            return redirect(user_dashboard)
        else:
            messages.warning(request, "Wrong username or password.")
            return render(request, "Userside/user_login.html", {"banner_data": banner_data, "categories_data": categories_data})
    else:
        return render(request, "Userside/user_login.html", {"banner_data": banner_data, "categories_data": categories_data})


def user_index(request):
    offer_data = AddOffers.objects.filter(is_showing=True)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    trendy_products = Product.objects.filter(is_teends_or_just_arived=True)
    just_arrive_products = Product.objects.filter(is_teends_or_just_arived=False)
    total_favourite_products = FavouriteProducts.objects.all().count()
    return render(request,"Userside/user_index.html",{"offer_data":offer_data,"categories_data":categories_data,"trendy_products":trendy_products,"just_arrive_products":just_arrive_products,"total_favourite_products":total_favourite_products,"banner_data":banner_data})
  
def user_dashboard(request):
    offer_data = AddOffers.objects.filter(is_showing=True)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    trendy_products = Product.objects.filter(is_teends_or_just_arived=True)
    just_arrive_products = Product.objects.filter(is_teends_or_just_arived=False)
    total_favourite_products = FavouriteProducts.objects.all().count()
    total_cart_items = Cart.objects.filter(user_id = request.user.id).count()
    return render(request,"Userside/user_dashboard.html",{"total_cart_items":total_cart_items,"offer_data":offer_data,"banner_data":banner_data,"categories_data":categories_data,"trendy_products":trendy_products,"just_arrive_products":just_arrive_products,"total_favourite_products":total_favourite_products})  

def user_logout(request):
    logout(request)
    messages.success(request,"Logout Successfully.")
    return redirect(user_dashboard)

def category_based_products(request,pk):
    offer_data = AddOffers.objects.filter(is_showing=True)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    filtered_products_according_category = Product.objects.filter(category_id = Category.objects.get(id=pk))
    print("Filtered products according to the category :- ", filtered_products_according_category)
    total_favourite_products = FavouriteProducts.objects.all().count()
    return render(request,"Userside/category_based_products.html",{"offer_data":offer_data,"banner_data":banner_data,"categories_data":categories_data,"filtered_products_according_category":filtered_products_according_category,"total_favourite_products":total_favourite_products})

def view_all_products(request):
    offer_data = AddOffers.objects.filter(is_showing=True)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    all_products = Product.objects.all()
    total_favourite_products = FavouriteProducts.objects.all().count()
    return render(request,"Userside/view_all_products.html",{"offer_data":offer_data,"banner_data":banner_data,"categories_data":categories_data,"all_products":all_products,"total_favourite_products":total_favourite_products})

def all_categories(request):
    offer_data = AddOffers.objects.filter(is_showing=True)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    all_categories = Category.objects.all()
    total_favourite_products = FavouriteProducts.objects.all().count()
    return render(request,"Userside/all_categories.html",{"offer_data":offer_data,"banner_data":banner_data,"categories_data":categories_data,"all_categories":all_categories,
    "total_favourite_products":total_favourite_products})

def product_details(request,pk):
    offer_data = AddOffers.objects.filter(is_showing=True)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    product_details = Product.objects.get(id=pk)
    print("Product Details :- ", product_details)
    total_favourite_products = FavouriteProducts.objects.all().count()
    return render(request,"Userside/product_details.html",{"offer_data":offer_data,"banner_data":banner_data,"categories_data":categories_data,"product_details":product_details,"total_favourite_products":total_favourite_products})

def add_to_favourite(request,pk):  
    selected_product = Product.objects.get(id=pk)
    fp = FavouriteProducts()
    fp.product_id = selected_product
    fp.save()
    return redirect(user_dashboard)


def all_favourite_products(request):
    offer_data = AddOffers.objects.filter(is_showing=True)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    filtered_all_favourite_products = FavouriteProducts.objects.all()
    total_favourite_products = FavouriteProducts.objects.all().count()
    return render(request,"Userside/all_favourite_products.html",{"offer_data":offer_data,"banner_data":banner_data,"categories_data":categories_data,"filtered_all_favourite_products":filtered_all_favourite_products,"total_favourite_products":total_favourite_products})

def remove_from_favourite(request,pk):
    selected_product =  FavouriteProducts.objects.get(id=pk)
    selected_product.delete()
    return redirect(all_favourite_products)


def contact_us(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        print(f"username = {username}")
        print(f"email = {email}")
        print(f"subject = {subject}")
        print(f"message = {message}")

        cu_user = ContactUs()
        cu_user.username= username
        cu_user.email = email
        cu_user.subject = subject
        cu_user.message = message
        cu_user.save()
        messages.success(request, "Your Query is Submitted successfully.")
        banner_data = AddBanner.objects.filter(is_show=True)
        categories_data = Category.objects.all()[:10]
        total_favourite_products = FavouriteProducts.objects.all().count()
        return render(request, 'Userside/contact_us.html',{"banner_data":banner_data,"categories_data":categories_data,"total_favourite_products":total_favourite_products})
    else:
        banner_data = AddBanner.objects.filter(is_show=True)
        categories_data = Category.objects.all()[:10]
        total_favourite_products = FavouriteProducts.objects.all().count()
        return render(request, "Userside/contact_us.html",{"banner_data":banner_data,"categories_data":categories_data,"total_favourite_products":total_favourite_products})

def about_us(request):
    offer_data = AddOffers.objects.filter(is_showing=True)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:10]
    total_favourite_products = FavouriteProducts.objects.all().count()
    return render(request,"Userside/about_us.html",{"offer_data":offer_data,"banner_data":banner_data,"categories_data":categories_data,"total_favourite_products":total_favourite_products})

def add_to_cart(request,pk):
    selected_product = Product.objects.get(id=pk)
    Quantity = 1
    c = Cart()
    c.user_id = User.objects.get(id = request.user.id)
    c.product_id = selected_product
    c.quantity = Quantity
    c.save()
    return redirect(user_dashboard)


def show_cart(request):
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    total_favourite_products = FavouriteProducts.objects.all().count()
    my_cart = Cart.objects.filter(user_id = request.user.id)
    total_cart_items = Cart.objects.filter(user_id = request.user.id).count()
    
    sub_total_price = 0
    shipping_charges = 10
    for i in my_cart:
        sub_total_price += int(i.product_id.product_price) * int(i.quantity)
    
    print("Sub total:- ", sub_total_price)
    total_price = shipping_charges + sub_total_price
    print("Total price:- ", total_price)

    return render(request,"Userside/show_cart.html",{
        "my_cart":my_cart,
        "banner_data":banner_data,
        "categories_data":categories_data,
        "total_favourite_products":total_favourite_products,
        "total_cart_items":total_cart_items,
        "sub_total_price":sub_total_price,
        "shipping_charges":shipping_charges,
        "total_price":total_price})

def remove_from_cart(request,pk):
    selected_product = Cart.objects.get(id=pk)
    selected_product.delete()
    return redirect(show_cart)

def increase_quantity(request,pk):
    selected_cart = Cart.objects.get(id=pk)
    selected_cart_quantity = int(selected_cart.quantity)
    print(type(selected_cart_quantity))

    selected_cart_quantity += 1
    
    selected_cart.quantity = str(selected_cart_quantity)
    selected_cart.save()
    return redirect(show_cart)

def decrease_quantity(request,pk):
    selected_cart = Cart.objects.get(id=pk)
    selected_cart_quantity = int(selected_cart.quantity)
    print(type(selected_cart_quantity))

    selected_cart_quantity -= 1
    
    selected_cart.quantity = str(selected_cart_quantity)
    selected_cart.save()
    return redirect(show_cart)

def user_checkout(request):
    total_cart_items = Cart.objects.filter(user_id = request.user.id).count()
    user_cart_items = Cart.objects.filter(user_id = request.user.id)
    
    sub_total_price = 0
    shipping_charges = 10
    
    for i in user_cart_items:
        sub_total_price += int(i.product_id.product_price) * int(i.quantity)
    
    print("Sub total:- ", sub_total_price)
    totalPrice = shipping_charges + sub_total_price
    print("Total price:- ", totalPrice)

    orderId = ''.join(random.choices(string.ascii_uppercase + string.digits,k=12))
    transactionId = ''.join(random.choices(string.ascii_uppercase + string.digits,k=12))    
    
    selected_cart = []
    for i in user_cart_items:
        print("Cart id:- ", i.id)
        selected_cart.append(Cart.objects.get(id=i.id))
    
    print("Selected Cart:- ", selected_cart)
    
    for j in selected_cart:
        o = Orders()
        o.user_id = User.objects.get(id=request.user.id)
        o.cart_id = j
        o.order_id = orderId
        o.transaction_id = transactionId
        o.total_payment = totalPrice
        o.save()
    
    messages.success(request,"Payment Successfull")
    return redirect(user_dashboard)

def order_details(request):
    orders_details = Orders.objects.filter(user_id=request.user.id)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    total_favourite_products = FavouriteProducts.objects.all().count()
    total_cart_items = Cart.objects.filter(user_id = request.user.id).count()
    return render(request,"Userside/order_details.html",{
        "orders_details":orders_details,
        "banner_data":banner_data,
        "categories_data":categories_data,
        "total_favourite_products":total_favourite_products,
        "total_cart_items":total_cart_items})

def orders_payment_details(request):
    payment_details = Orders.objects.filter(user_id=request.user.id)
    banner_data = AddBanner.objects.filter(is_show=True)
    categories_data = Category.objects.all()[:15]
    total_favourite_products = FavouriteProducts.objects.all().count()
    total_cart_items = Cart.objects.filter(user_id = request.user.id).count()
    return render(request,"Userside/orders_payment_details.html",{
        "payment_details":payment_details,
        "banner_data":banner_data,
        "categories_data":categories_data,
        "total_favourite_products":total_favourite_products,
        "total_cart_items":total_cart_items})

def user_profile(request,pk):
    logged_in_user_data = User.objects.get(id=pk)
    logged_in_user_profile = UserProfile.objects.get(userId=request.user.id)
    print("Logged in user profile:- ", logged_in_user_profile)
    print("User id:- ", logged_in_user_profile.userId, "User image:- ", logged_in_user_profile.user_image,"Phone number:- ", logged_in_user_profile.phone_number, "Address:- ", logged_in_user_profile.address, "Pincode:- ", logged_in_user_profile.pincode, "Locality:- ", logged_in_user_profile.locality)
    
    if request.method == 'POST':
        print("Inside the POST method")

        admin_profile_image = request.FILES["adminprofileimage"]
        firstName = request.POST["firstname"]
        lastName = request.POST["lastname"]
        adminEmail = request.POST["adminemail"]
        phoneNumber = request.POST["phonenumber"]
        adminAddress = request.POST["adminaddress"]
        admin_locality = request.POST["locality"]
        pincode = request.POST["pincode"]
        
        print("First name:- ", firstName)

        logged_in_user_data.first_name = firstName
        logged_in_user_data.last_name = lastName
        logged_in_user_data.email = adminEmail
        logged_in_user_data.save()

        logged_in_user_profile.user_image = admin_profile_image
        logged_in_user_profile.phone_number = phoneNumber
        logged_in_user_profile.address = adminAddress
        logged_in_user_profile.locality = admin_locality
        logged_in_user_profile.pincode = pincode
        logged_in_user_profile.save()
        
        messages.success(request,"Admin profile updated successfully.")
        return render(request, "Userside/user_profile.html",{
            "user_profile":logged_in_user_profile,"logged_in_user_data":logged_in_user_data})
    else:
        banner_data = AddBanner.objects.filter(is_show=True)
        categories_data = Category.objects.all()[:15]
        total_favourite_products = FavouriteProducts.objects.all().count()
        total_cart_items = Cart.objects.filter(user_id = request.user.id).count()
        print("Inside the Else functionality")
        return render(request, "Userside/user_profile.html",{
            "user_profile":logged_in_user_profile,"logged_in_user_data":logged_in_user_data,"banner_data":banner_data,
        "categories_data":categories_data,
        "total_favourite_products":total_favourite_products,
        "total_cart_items":total_cart_items})
