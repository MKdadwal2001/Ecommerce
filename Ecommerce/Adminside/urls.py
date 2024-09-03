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

]