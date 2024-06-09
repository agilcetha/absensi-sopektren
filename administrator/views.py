from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from dashboard.decorators import ijinkan_pengguna,pilihan_login
from .models import Peserta
from .form import FormPeserta 

# Create your views here.

@login_required(login_url='loginPage')
@pilihan_login
def beranda_admin(request):
    context={
        'judul':'halaman beranda admin'
    }
    return render(request, 'beranda_admin.html', context)

@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def data_peserta(request):
    data = Peserta.objects.order_by('-id')
    context={
        'judul':'halaman data peserta',
        'data': data
    }
    return render(request, 'data_peserta.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def jadwal_absen(request):
    context={
        'judul':'halaman data peserta'
    }
    return render(request, 'jadwal_absen.html', context)

@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def rekap_absen(request):
    context={
        'judul':'halaman data peserta'
    }
    return render(request, 'rekap_absen.html', context)

@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def tambah_peserta(request):
    form = FormPeserta
    if request.method == "POST":
        simpan = FormPeserta(request.POST)
        if simpan.is_valid():
            simpan.save()
            return redirect('data_peserta')
    context={
        'judul':'halaman data peserta',
        'form': form
    }
    return render(request, 'tambah_peserta.html', context)

@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def edit_peserta(request,pk):
    editpeserta= Peserta.objects.get(id=pk)
    form = FormPeserta(instance=editpeserta)
    if request.method == "POST":
        simpan = FormPeserta(request.POST, instance=editpeserta)
        if simpan.is_valid():
            simpan.save()
            return redirect('data_peserta')
    context={
        'judul':'halaman data peserta',
        'form': form
    }
    return render(request, 'tambah_peserta.html', context)

@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def hapus_peserta(request,pk):
    editpeserta= Peserta.objects.get(id=pk)
    if request.method == "POST":
        editpeserta.delete()
        return redirect('data_peserta')
    context={
        'judul':'halaman data peserta',
        'editpeserta':editpeserta
    }
    return render(request, 'hapus_peserta.html', context)