from django.urls import path
from . import views

urlpatterns = [
    path("user-index",views.user_index,name="user-index"),
    path("user-dashboard",views.user_dashboard,name="user-dashboard"),
    path("user-login",views.user_login,name="user-login"),
    path("user-register",views.user_register,name="user-register"),
    path("user-logout",views.user_logout, name="user-logout"),

    path("category-based-products/<int:pk>",views.category_based_products,name="category-based-products"),
    path("all-products",views.view_all_products,name="all-products"),
    path("all-categories",views.all_categories,name="all-categories"),
    path("product-details/<int:pk>",views.product_details,name="product-details"),
    path("add-to-favourite/<int:pk>",views.add_to_favourite,name="add-to-favourite"),
    path("all-favourite-products",views.all_favourite_products,name="all-favourite-products"),
    path("remove-from-favourite/<int:pk>",views.remove_from_favourite,name="remove-from-favourite"),
    
    path("contact-us",views.contact_us,name="contact-us"),
    path("about-us",views.about_us,name="about-us"),
     
]
