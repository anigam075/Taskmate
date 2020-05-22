from django.contrib import admin
from django.urls import path, include
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist.urls')), 
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('account/', include('users.urls')),
]
