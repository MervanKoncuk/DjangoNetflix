from django.shortcuts import render
from .models import *
from user.models import *
from django.db.models import Q
# Create your views here.
def index(request):
    print(request.path)
    return render(request, "index.html")

def movies(request):
    profile = request.user
    filmler = Movie.objects.all()
    filmlerim = MyMovie.objects.get(owner = profile.id)
    izlenen = filmlerim.movie.all()


    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    filmler = Movie.objects.filter(
        Q(name__icontains = search_query) |
        Q(ekleyen__icontains = search_query) |
        Q(sub_category__name__icontains = search_query)
    )
    context = {
        'movie':filmler,
        'search':search_query,
        'filmler':izlenen
    }
    
    
    return render(request, "movies.html", context)
def secimler(request):
    profile = request.user
    users = Sub_user.objects.filter(owner = profile.id)
    return render(request, "profiles.html", {'users':users})

