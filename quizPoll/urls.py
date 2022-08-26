from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name="registration"),
    path('login_page', views.login_page, name="login_page"),
    path('homepage', views.homepage, name="homepage"),
    path('add_poles', views.add_poles, name="add_poles"),
    path('vote/<id>', views.vote, name="vote"),
    path('result/<id>', views.result, name="result"),
    path('logoutView', views.logoutView, name="logoutView"),
    path('my_profile', views.my_profile, name="my_profile")
]