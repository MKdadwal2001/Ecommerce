from django.urls import path
from . import views

urlpatterns = [
    path("admin-login",views.admin_login,name="admin-login"),
    path("admin-logout",views.admin_logout,name="admin-logout"),
    
    path("admin-index",views.admin_index,name="admin-index"),

    path("add-category",views.add_category,name="add-category"),
    path("show-categories",views.show_categories,name="show-categories"),
    path("delete-category/<int:pk>",views.delete_category,name="delete-category"),
    path("update-category/<int:pk>",views.update_category,name="update-category"),

    path("add-product",views.add_product,name="add-product"),
    path("show-products",views.show_products,name="show-products"),
    path("delete-product/<int:pk>",views.delete_product,name="delete-product"),
    path("update-product/<int:pk>",views.update_product,name="update-product"),
    path("customer-queries",views.customer_queries,name="customer-queries"),
    path("admin-reply-customer-queries/<int:pk>",views.admin_reply_customer_queries,name="admin-reply-customer-queries"),

    path("add-banner",views.add_banner,name="add-banner"),
    path("show-banner",views.show_banner,name="show-banner"),
    path("update-banner/<int:pk>",views.update_banner,name="update-banner"),
    path("delete-banner/<int:pk>",views.delete_banner,name="delete-banner"),
   
    path("add-offer",views.add_offer,name="add-offer"),
    path("show-offer",views.show_offer,name="show-offer"),
    path("update-offer/<int:pk>",views.update_offer,name="update-offer"),
    path("delete-offer/<int:pk>",views.delete_offer,name="delete-offer"),

    path("admin-profile/<int:pk>", views.admin_profile, name="admin-profile"),
    
    path('product-description/', views.product_description, name='product-description'),

    path("customers-orders",views.customers_orders,name="customers-orders"),
    path("payment-details",views.payment_details,name="payment-details"),
]