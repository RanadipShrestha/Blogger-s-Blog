from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('article/<int:id>/', views.article_detail, name="article_detail"),

    path('blog/', views.blog, name="blog"),
    path('blog/<slug:slug>/', views.blog, name="category_blog"),

    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    path("register/", views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    
    path('blog/<slug:slug>/', views.blog, name="blog_with_slug"),
]