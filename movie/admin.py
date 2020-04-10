from django.contrib import admin

# Register your models here.
from .models import Movie, Movie_links
admin.site.register(Movie)
admin.site.register(Movie_links)
