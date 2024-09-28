from django.urls import path
from index_page import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="business"),
    path("fame", views.hall_of_fame,name="Hall_of_fame"),
    path("Services",views.Services,name= "Services"),
    path("signin",views.signin,name= "Signin"),
    path("login",views.login,name="Login"),
    path("aboutus", views.AboutUs, name="AboutUs"),
]