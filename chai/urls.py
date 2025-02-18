from django.contrib import admin
from django.urls import path, include
from .import views

# localshost: 8000/chai
# localhost: 8000/chai/order

urlpatterns = [
    path("", views.all_chai, name='all_chai'),
    path("myadmin/", admin.site.urls), 
]
