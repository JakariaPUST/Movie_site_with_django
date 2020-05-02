from django.shortcuts import render

from django.views.generic import ListView,DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie, MovieLinks

class MovieList(ListView):
	model = Movie
	paginate_by =2

class MovieDetail(DetailView):
	model = Movie

	def get_object(self):
		object = super(MovieDetail, self).get_object()
		object.views_count +=1
		object.save()
		return object

	def get_context_data(self, **kwargs):
		context = super(MovieDetail, self).get_context_data(**kwargs)
		context['links'] = MovieLinks.objects.filter(movie=self.get_object())
		return context

class MovieCategory(ListView):
	paginate_by =2
	model = Movie
	def get_queryset(self):
		self.category = self.kwargs['category']
		movies = Movie.objects.filter(category=self.category)
		return movies
	def get_context_data(self, **kwargs):
	    context = super(MovieCategory, self).get_context_data(**kwargs)
	    context['movie_category'] = self.category
	    return context

class MovieLanguage(ListView):
	paginate_by =2
	model = Movie
	def get_queryset(self):
		self.language = self.kwargs['language']
		movies = Movie.objects.filter(language=self.language)
		return movies
	def get_context_data(self, **kwargs):
	    context = super(MovieLanguage, self).get_context_data(**kwargs)
	    context['language'] = self.language
	    return context

class MovieSearch(ListView):
	paginate_by =2
	model = Movie
	template_name = 'test.html'

	def get_queryset(self):
		query =self.request.GET.get('query')
		if query :
			object_list = Movie.objects.filter(title__icontains=query)
			print(query)
			print(object_list)
		else :
			object_list = self.model.objects.none()
		return object_list

class MovieYear(YearArchiveView):
	queryset = Movie.objects.all()
	date_field = "year_of_production"
	make_object_list = True
	allow_future = True
	print(queryset)