from django.shortcuts import render,redirect
from django.contrib import messages 

# Create your views here.
from .models import *

def home(request):
    return render(request,'index.html')
    
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Basic validation
        if not name or not email or not message:
            messages.error(request, "All fields are required.")
            return render(request, 'index.html')

        # Save the form data to the ContactForm model
        ContactForm.objects.create(name=name, email=email, message=message)

        messages.success(request, "Your message has been received successfully!")
        return redirect('home')  # Redirect to avoid duplicate submissions

    return render(request, 'index.html')