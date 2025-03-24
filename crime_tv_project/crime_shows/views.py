from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import CrimeShow
from django.contrib.auth.decorators import login_required

# View to display the list of crime shows
def crime_show_list(request):
    crime_shows = CrimeShow.objects.all()
    return render(request, 'crime_shows/crime_show_list.html', {'crime_shows': crime_shows})

# View to display the details of a single crime show
def crime_show_detail(request, pk):
    crime_show = CrimeShow.objects.get(pk=pk)
    return render(request, 'crime_shows/crime_show_detail.html', {'crime_show': crime_show})

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'crime_shows/register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crime_show_list')
        else:
            return redirect('login')
    return render(request, 'crime_shows/login.html')

# User logout view
def logout_view(request):
    logout(request)
    return redirect('crime_show_list')

# View to allow authenticated users to add a new crime show
@login_required
def add_crime_show(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        genre = request.POST['genre']
        release_date = request.POST['release_date']
        rating = request.POST['rating']
        image = request.FILES['image']
        added_by = request.user
        CrimeShow.objects.create(
            title=title,
            description=description,
            genre=genre,
            release_date=release_date,
            rating=rating,
            image=image,
            added_by=added_by
        )
        return redirect('crime_show_list')
    return render(request, 'crime_shows/add_crime_show.html')
