from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import CrimeShow
from .contact import ContactForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

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

# View to allow authenticated users to delete a crime show
@login_required
def delete_crime_show(request, pk):
    crime_show = CrimeShow.objects.get(pk=pk)
    if request.method == 'POST':
        crime_show.delete()
        return redirect('crime_show_list')
    return redirect('crime_show_detail', pk=pk)

# Contact
def contact(request):
	submitted = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@dcu.ie'),
				['rebecca.mchugh32@mail.dcu.ie'],
				connection=con
			)
			return HttpResponseRedirect(reverse('contact') + '?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
        'crime_shows': CrimeShow.objects.all(),
		'submitted': submitted
	}
	return render(request, 'crime_shows/contact.html', context)