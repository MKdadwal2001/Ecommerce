from django.urls import path
from . import views

urlpatterns = [
    path("index",views.index,name="index"),
    path("user-dashboard",views.user_dashboard,name="user-dashboard"),
    path("user-login",views.user_login,name="user-login"),
    path("user-register",views.user_register,name="user-register"),
]
