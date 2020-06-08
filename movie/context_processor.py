from .models import Movie

def Slider_movie(request):
	# movie = Movie.objects.all().order_by('created')[0:5]
	movie = Movie.objects.last()
	return {'slider_movie': movie}
