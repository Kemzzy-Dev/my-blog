
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('blog.html/', views.blog, name='blog'),
    path('contact.html/', views.contacts, name='contact'),
    path('<slug:slug>', views.details, name='details'),
    path('category/<str:str>', views.category, name='category'),
    path('drafts.html/', views.drafts, name='drafts'),
]