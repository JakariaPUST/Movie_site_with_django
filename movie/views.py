from django.shortcuts import render

from django.views.generic import ListView,DetailView
from .models import Movie 
class MovieList(ListView):
	model = Movie
	paginate_by =1 
class MovieDetail(DetailView):
	model = Movie
	#template_name=''