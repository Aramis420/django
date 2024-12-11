from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(label='Nombre y apellido',
    required=True,
    min_length=5,
    max_length=25,
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'Ingrese su Nombre y Apellido'}))

    email=forms.EmailField(label='Correo',
    required=True,
    min_length=5,
    max_length=40,
    widget=forms.EmailInput(attrs={'class': 'form-control',
    'placeholder':'Ingrese su Correo'}))

    message=forms.CharField(label='message',
    required=True,
    min_length=5,
    max_length=50,
    widget=forms.Textarea(attrs={'class': 'form-control',
    'placeholder':'Ingrese su Mensaje','row':5}))
