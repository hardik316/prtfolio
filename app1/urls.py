from django.contrib import admin
from django.urls import path
from .views import home,contact_form
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name='home'),
    path('contact/',contact_form, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)