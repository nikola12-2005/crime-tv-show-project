from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'), # Contact page
    path('', views.crime_show_list, name='crime_show_list'),  # List of all crime shows
    path('show/<int:pk>/', views.crime_show_detail, name='crime_show_detail'),  # Show details
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('add/', views.add_crime_show, name='add_crime_show'),  # Add new crime show
    path('delete/<int:pk>/', views.delete_crime_show, name='delete_crime_show'), # Remove crime show
]
