from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from signup import views

urlpatterns = [
    path("/signup",views.signup,name='signup')
]