from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Sub_user(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to="Sub/", null=True, blank=True, verbose_name="Profil resmi")
    
    def __str__(self):
        return self.name