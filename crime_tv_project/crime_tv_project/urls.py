from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


def home_redirect(request):
    return redirect("crime_show_list")

urlpatterns = [
    path("", home_redirect, name="home"),
    path('admin/', admin.site.urls),  # Django admin page
    path('crime_shows/', include('crime_shows.urls')),  # Main route for the crime_shows app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
