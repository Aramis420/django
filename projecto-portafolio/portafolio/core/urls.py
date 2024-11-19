from django.urls import path, include
from core import views as core_views
urlpatterns = [
    path('', core_views.home, name='home'),
    path('contact/',core_views.contact,name='contacto'),
    path('login/',core_views.login, name='login'),
    path('register/',core_views.register, name='register'),
    path('blog/',core_views.blog,name="blog"),
    path('category/<int:category_id>/',core_views.category,name="category"),
]