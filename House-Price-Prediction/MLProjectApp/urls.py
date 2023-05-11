from django.contrib import admin
from django.urls import path
from MLProjectApp import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("predict", views.predict, name='predict'),
    path("predict/prediction", views.prediction, name='prediction')
]