from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')