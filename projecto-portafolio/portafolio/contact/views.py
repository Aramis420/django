from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .form import ContactForm 

# Create your views here.
def contact(request):
    contact_form=ContactForm
    return render(request,'contact/contact.html',{'form':contact_form})