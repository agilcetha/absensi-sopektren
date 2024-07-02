from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.decorators import ijinkan_pengguna, pilihan_login
from .models import Peserta, Prodi, Fakultas
from .form import FormPeserta, FormJadwalAbsensi

# Create your views here.


@login_required(login_url='loginPage')
@pilihan_login
def beranda_admin(request):
    jumlah_peserta = Peserta.objects.count()
    jumlah_prodi = Prodi.objects.count()
    jumlah_fakultas = Fakultas.objects.count()
    context = {
        'judul': 'Halaman Beranda',
        'menu': 'beranda_admin',
        'jumlah_peserta': jumlah_peserta,
        'jumlah_prodi': jumlah_prodi,
        'jumlah_fakultas': jumlah_fakultas,

    }
    return render(request, 'beranda_admin.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def data_peserta(request):
    data = Peserta.objects.order_by('-id')
    context = {
        'judul': 'halaman data peserta',
        'data': data,
        'menu': 'data_peserta'
    }
    return render(request, 'data_peserta.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def data_fakultas(request):
    data_prodi = Prodi.objects.order_by('-id')
    fakultas = Fakultas.objects.order_by('-id')
    context = {
        'judul': 'Halaman Data Fakultas',
        'data_prodi': data_prodi,
        'fakultas': fakultas,
        'menu': 'data_fakultas'
    }
    return render(request, 'data_fakultas.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def jadwal_absen(request):
    if request.method == 'POST':
        form = FormJadwalAbsensi(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jadwal_absen')
    else:
        form = FormJadwalAbsensi()

    context = {
        'judul': 'Halaman Penjadwalan',
        'menu': 'jadwal_absensi',
        'form_jadwal': form
    }
    return render(request, 'jadwal_absen.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def rekap_absen(request):
    context = {
        'judul': 'Halaman Rekap Absensi',
        'menu': 'rekap_absen'
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
    context = {
        'judul': 'halaman data peserta',
        'form': form
    }
    return render(request, 'tambah_peserta.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def edit_peserta(request, pk):
    editpeserta = Peserta.objects.get(id=pk)
    form = FormPeserta(instance=editpeserta)
    if request.method == "POST":
        simpan = FormPeserta(request.POST, instance=editpeserta)
        if simpan.is_valid():
            simpan.save()
            return redirect('data_peserta')
    context = {
        'judul': 'halaman data peserta',
        'form': form
    }
    return render(request, 'tambah_peserta.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def hapus_peserta(request, pk):
    editpeserta = Peserta.objects.get(id=pk)
    editpeserta.delete()
    return redirect('data_peserta')


# @ijinkan_pengguna(yang_diizinkan=['administrator'])
# @login_required(login_url='loginPage')
# def hapus_peserta(request,pk):
#     editpeserta= Peserta.objects.get(id=pk)
#     if request.method == "POST":
#         editpeserta.delete()
#         return redirect('data_peserta')
#     context={
#         'judul':'halaman data peserta',
#         'editpeserta':editpeserta
#     }
#     return render(request, 'hapus_peserta.html', context)
