from django.contrib import admin
from django.urls import path
from .views import home,contact_form

urlpatterns = [
    path('',home, name='home'),
    path('contact/',contact_form, name='contact'),
]