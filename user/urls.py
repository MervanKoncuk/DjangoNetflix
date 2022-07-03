from django.urls import path
from movies.views import *
from .views import *
urlpatterns = [
    path("login/", giris, name="login"),
    path("register/", register, name="register"),
    path("profile/", profile, name="user"),
    path("logout/", cikis, name="logout"),
    path("hesapSil/", hesapSilme, name="hesapSil"),
]