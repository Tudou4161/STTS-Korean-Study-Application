from django.urls import path
from django.contrib import admin
from main_app import views

app_name = "main_app"

urlpatterns = [
    path('', views.main, name="main"),
]