from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Sub_category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Movie(models.Model):
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to="filmler/", null=True, blank=True, verbose_name="Film Resmi")
    name = models.CharField(max_length=200)
    ekleyen = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class MyMovie(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    movie = models.ManyToManyField("Movie", related_name="mymovie")