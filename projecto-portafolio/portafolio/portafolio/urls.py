"""
URL configuration for portafolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from portfolio import views as portfolio_views
from about import views as about_views
from contact import views as contact_views
# el "as" es por la redundancia de nombres
urlpatterns = [
    path('', include('core.urls')),
    path('about-me/',about_views.about,name='about-me'),
    path('portfolio/',portfolio_views.portfolio,name='portfolio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("contact/", contact_views.contact, name="contact"),
    path('admin/',admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static
#Arregla error 404 que no encutra imagen y no muestra display al ver imagen en pag admin.
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)