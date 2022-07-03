from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import *
# Create your views here.
def giris(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
  
        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş yaptınız')
            return redirect('Secim')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
    return render(request, "login.html")
def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            # create your user
            user.save()
            messages.success(request, 'Giriş yaptınız!')
            return redirect('login')
        else:
            messages.success(request, 'Lütfen hatalı alanları düzeltiniz!')
    return render(request, "register.html", {'form': form})

def profile(request):
    profile = request.user
    if profile.is_authenticated:
        return render(request, "hesap.html", {'profile':profile})
    else: 
        return redirect('login')

def cikis(request):
    logout(request)
    return redirect('index')

def hesapSilme(request):
    profile = request.user
    if profile.is_authenticated:
        user = User.objects.get(id = profile.id)
        user.delete()
        messages.success(request, 'Hesabınız silindi!')
        return redirect('index')
    else:
        return redirect('login')
