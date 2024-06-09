from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .decorators import tolakhalaman_ini

@tolakhalaman_ini
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'Username Tidak ditemukan')
            return redirect('loginPage')
        cocokan = authenticate(request, username=username, password=password)
        if cocokan is None:
            messages.success(request, 'Password salah')
            return redirect('loginPage')
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda_admin')
    context = {
    'judul': 'Halaman Login',
    }
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('loginPage')