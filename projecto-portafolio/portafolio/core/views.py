from django.shortcuts import render,HttpResponse

# Create your views here.
html_cabecera="""
<h1>Mi Portafolio Personal</h1>
<ul>
    <li> <a href="/">Inicio</a> </li>
    <li> <a href="/about-me/">Acerca de</a> </li>
    <li> <a href="/portfolio/">Portafolio</a> </li>
    <li> <a href="/contact/">Contacto</a> </li>
</ul>
"""

def home(request):
    return render(request,'core/home.html')

def contact(request):
    return render(request,'core/contact.html')
