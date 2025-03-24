from django.db import models
from django.contrib.auth.models import User

class CrimeShow(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(upload_to='crime_shows/', null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow null values

    def __str__(self):
        return self.title
