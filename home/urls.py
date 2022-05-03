from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.loginpage,name='loginpage'),
    path('signup', views.signup,name='signup'),
    path('login', views.loginUser,name='loginUser'),
    # path('logout', views.logoutUser,name='logoutUser'),
]

