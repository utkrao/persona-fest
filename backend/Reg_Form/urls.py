from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.form, name = "form"),
    path('register/', views.registration, name = "registration"),
    path('saveform/', views.saveform, name = "saveform"),


    # path('', views.saveform, name = "form"),

]