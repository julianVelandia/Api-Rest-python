from django.contrib import admin
from django.urls import path

from perfiles_api import views

urlpatterns = [
    path('hello/', views.HelloApiview.as_view()),
]
