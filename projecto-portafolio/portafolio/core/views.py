from django.shortcuts import render,HttpResponse, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .models import Posteo,Clasificacion
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
def editingproj(request):
    return render(request,'admin/portfolio/project')
def home(request):
    return render(request,'core/home.html')
def login(request):
    return render(request,'core/login.html')
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user = user_creation_form.save(commit=False)
            user.is_staff = True
            user.save()
            group = Group.objects.get(name='Team Projectos')  # Cambia "NombreDelGrupo" por el nombre de tu grupo
            user.groups.add(group)
            
            return redirect('login')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

def blog(request):
    posts=Posteo.objects.all()
    category=Clasificacion.objects.all()
    return render(request,"core/blog.html",{'posts':posts,
    'category':category})

def category(request,category_id):
    category=get_object_or_404(Clasificacion,id=category_id)
    posts=Posteo.objects.filter(classification=category)
    return render(request,"core/category.html",{'posts':posts,'category':category})


