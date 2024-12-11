from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .form import ContactForm

def contact(request):
    contact_form=ContactForm()
    if request.method == 'POST':
        contact_form=ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('mensaje', '')

            email=EmailMessage(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
                email,
                ['0b47ade9eaf29f@inbox.mailtrap.io'],
                reply_to=[email],
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok',{'form':contact_form})
            except:
                return redirect(reverse('contact')+'?error')

    return render(request,'contact/contact.html', {'form':contact_form})
