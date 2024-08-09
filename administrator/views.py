from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from dashboard.decorators import ijinkan_pengguna, pilihan_login
from .models import *
from .form import FormPeserta, FormJadwalAbsensi
from django.contrib.auth.models import User, Group

# Create your views here.

# Fungsi untuk beranda


@login_required(login_url='loginPage')
@pilihan_login
def beranda_admin(request):
    jumlah_peserta = Peserta.objects.filter(status_mahasiswa='Sudah').count()
    jumlah_prodi = Prodi.objects.count()
    jumlah_fakultas = Fakultas.objects.count()
    peserta = Peserta.objects.filter(status_mahasiswa='Belum').order_by('-id')

    context = {
        'judul': 'Halaman Beranda',
        'menu': 'beranda_admin',
        'jumlah_peserta': jumlah_peserta,
        'jumlah_prodi': jumlah_prodi,
        'jumlah_fakultas': jumlah_fakultas,
        'peserta': peserta

    }
    return render(request, 'beranda_admin.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def konfirmasi(request, pk):
    data = get_object_or_404(Peserta, id=pk)

    # Update status mahasiswa menjadi 'Sudah'
    data.status_mahasiswa = 'Sudah'
    data.save()

    # Cek apakah user dengan username yang sama sudah ada
    if not User.objects.filter(username=data.nomor_induk_mahasiswa).exists():
        # Buat user baru
        user = User.objects.create_user(
            username=data.nomor_induk_mahasiswa,
            password=data.password,
            first_name=data.nama_mahasiswa
            
        )

        # Tambahkan user ke grup "peserta"
        group, created = Group.objects.get_or_create(name='peserta')
        user.groups.add(group)

        # Update peserta untuk mengaitkan dengan user yang baru dibuat
        data.user = user
        data.save()

    return redirect('data_peserta')


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def batal(request, pk):
    data = Peserta.objects.get(id=pk)
    data.delete()
    return redirect('beranda_admin')
# ---------------------------------------------------------#

# Fungsi untuk data peserta


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def data_peserta(request):
    data = Peserta.objects.filter(status_mahasiswa='Sudah').order_by('-id')
    context = {
        'judul': 'halaman data peserta',
        'data': data,
        'menu': 'data_peserta'
    }
    return render(request, 'data_peserta.html', context)


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

# ------------------------------------------------------------

# fungsi data peserta


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
# -------------------------------------------------------------

# fungsi untuk jadwal absensi


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def jadwal_absen(request):
    jadwal = JadwalAbsensi.objects.all().order_by('-id')
    if request.method == 'POST':
        form = FormJadwalAbsensi(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail_jadwal')
    else:
        form = FormJadwalAbsensi()

    context = {
        'judul': 'Halaman Penjadwalan',
        'menu': 'jadwal_absensi',
        'form_jadwal': form,
        'jadwal': jadwal
    }
    return render(request, 'jadwal_absen.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def detail_jadwal(request):
    jadwal = JadwalAbsensi.objects.all().order_by('-id')

    context = {
        'judul': 'Halaman Detail Jadwal',
        'menu': 'detail_jadwal',
        'jadwal': jadwal

    }
    return render(request, 'detail_jadwal.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def hapus_jadwal(request, pk):
    hps_jadwal = JadwalAbsensi.objects.get(id=pk)
    hps_jadwal.delete()
    return redirect('jadwal_absensi')


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def rekap_absen(request):
    rekap = RekapAbsen.objects.all()
    jumlah_peserta = Peserta.objects.count()
    tanggal_absensi = JadwalAbsensi.objects.all()
    # order_by('tanggal').values_list('tanggal', flat=True).distinct()
    context = {
        'judul': 'Halaman Rekap Absensi',
        'menu': 'rekap_absen',
        'rekap': rekap,
        'jumlah_peserta': jumlah_peserta,
        'tanggal': tanggal_absensi
    }
    return render(request, 'rekap_absen.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def rekap_absen2(request):
    jadwal_absensi = JadwalAbsensi.objects.all()
    context = {
        'jadwal_absensi': jadwal_absensi
    }
    return render(request, 'rekap_absen2.html', context)


@ijinkan_pengguna(yang_diizinkan=['administrator'])
@login_required(login_url='loginPage')
def rekap_view(request, pk):
    jadwal_absensi = JadwalAbsensi.objects.get(id=pk)
    jumlah_peserta = Peserta.objects.filter(status_mahasiswa='Sudah').count()

    # Ambil semua rekap absensi untuk jadwal_absensi tertentu
    rekap_absensi = RekapAbsen.objects.filter(
        jadwal_absensi=jadwal_absensi).select_related('data_mahasiswa__peserta')

    # Data untuk ditampilkan di template
    peserta_absensi = {}

    for rekap in rekap_absensi:
        peserta = rekap.data_mahasiswa.peserta
        if peserta not in peserta_absensi:
            peserta_absensi[peserta] = {'checkin': '-', 'checkout': '-'}
        if rekap.type_absensi == 'checkin':
            peserta_absensi[peserta]['checkin'] = rekap.status_absensi
        elif rekap.type_absensi == 'checkout':
            peserta_absensi[peserta]['checkout'] = rekap.status_absensi

    context = {
        'judul': 'Halaman Rekap Absen',
        'jadwal_absensi': jadwal_absensi,
        'jumlah_peserta': jumlah_peserta,
        'jumlah_checkin': rekap_absensi.filter(type_absensi='checkin').count(),
        'jumlah_checkout': rekap_absensi.filter(type_absensi='checkout').count(),
        'peserta_absensi': peserta_absensi
    }

    return render(request, 'rekap_view.html', context)


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
