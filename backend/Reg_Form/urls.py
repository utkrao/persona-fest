from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.form, name = "form"),
    path('register/', views.registration, name = "registration"),
    path('management/', views.management, name = "management"),
    path('design/', views.design, name = "design"),
    path('architecture/', views.architecture, name = "architecture"),
    path('food/', views.food, name = "food"),
    path('saveform/', views.saveform, name = "saveform"),
    path('technical/', views.technical, name = "technical"),
    path('success/', views.success, name = "success"),
    # path('Contactus/', views.Contactus, name = "Contactus"),
    # path('', views.saveform, name = "form"),

]