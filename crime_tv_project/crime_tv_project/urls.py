# crime_tv_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect("crime_show_list")

urlpatterns = [
    path("", home_redirect, name="home"),
    path('admin/', admin.site.urls),  # Django admin page
    path('crime_shows/', include('crime_shows.urls')),  # Main route for the crime_shows app
]
