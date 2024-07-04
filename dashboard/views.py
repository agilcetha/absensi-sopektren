from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .decorators import tolakhalaman_ini
from administrator.form import FormRegister


@tolakhalaman_ini
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
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


def registerPage(request):
    form = FormRegister
    if request.method == "POST":
        simpan = FormRegister(request.POST,request.FILES)
        if simpan.is_valid():
            simpan.save()
            messages.success(request, "Registrasi berhasil. Selanjutnya Mohon Tunggu Informasi Dari Admin")
            return redirect('loginPage')
        else:
            messages.success(request, "Register gagal")
            return redirect('registerPage')
    context = {
        'judul': 'Halaman Register',
        'form': form
    }
    return render(request, 'register.html', context)
