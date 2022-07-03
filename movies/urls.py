from django.urls import path
from movies.views import *

urlpatterns = [
    path("", index, name="index"),
    path("movies/", movies, name="Movie"),
    path("secim", secimler, name="Secim"),
    
]