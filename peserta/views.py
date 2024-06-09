from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.decorators import ijinkan_pengguna


# Create your views here.

@login_required(login_url='loginPage')
@ijinkan_pengguna(yang_diizinkan=['peserta'])
def beranda_peserta(request):
    context={
        'judul':'halaman login'
    }
    return render(request, 'beranda_peserta.html', context)

@ijinkan_pengguna(yang_diizinkan=['peserta'])
@login_required(login_url='loginPage')
def absensi(request):
    context={
        'judul':'halaman login'
    }
    return render(request, 'absensi.html', context)

@ijinkan_pengguna(yang_diizinkan=['peserta'])
@login_required(login_url='loginPage')
def sertifikat(request):
    context={
        'judul':'halaman login'
    }
    return render(request, 'sertifikat.html', context)