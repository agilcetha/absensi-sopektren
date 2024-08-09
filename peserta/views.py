from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from dashboard.decorators import ijinkan_pengguna
from administrator.form import FormBerandaPeserta
from administrator.models import *
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime,date
from django.contrib import messages
from .utils import cek_kehadiran
from .utils import generate_certificate_pdf
from django.conf import settings






@login_required(login_url='loginPage')
@ijinkan_pengguna(yang_diizinkan=['peserta'])
def beranda_peserta(request):
    
    # Mengambil data peserta yang sedang login
    berandapeserta = get_object_or_404(Peserta, user=request.user)

    # Membuat form dengan instance data peserta
    form = FormBerandaPeserta(instance=berandapeserta)
    
    if request.method == "POST":
        # Menyimpan data dari form
        simpan = FormBerandaPeserta(request.POST, instance=berandapeserta)
        if simpan.is_valid():
            simpan.save()
            return redirect('beranda_peserta')
    
    context = {
        'judul': 'Halaman Data Peserta',
        'form': form
    }
    return render(request, 'beranda_peserta.html', context)


@login_required(login_url='loginPage')
@ijinkan_pengguna(yang_diizinkan=['peserta'])
def absensi(request):
    jadwal_absensi = JadwalAbsensi.objects.all()
    now = timezone.now()
    today = date.today()

    # Proses jadwal untuk menambahkan status absensi
    jadwal_list = []
    for x in jadwal_absensi:
        checkin_mulai = timezone.make_aware(
            timezone.datetime.combine(x.tanggal, x.checkin_mulai)
        )
        checkin_selesai = timezone.make_aware(
            timezone.datetime.combine(x.tanggal, x.checkin_selesai)
        )
        checkout_mulai = timezone.make_aware(
            timezone.datetime.combine(x.tanggal, x.checkout_mulai)
        )
        checkout_selesai = timezone.make_aware(
            timezone.datetime.combine(x.tanggal, x.checkout_selesai)
        )

        x.is_checkin_valid = checkin_mulai <= now <= checkin_selesai
        x.is_checkout_valid = checkout_mulai <= now <= checkout_selesai

        jadwal_list.append(x)

    if request.method == 'POST':
        jadwal_id_checkin = request.POST.get('jadwal_id_checkin')
        jadwal_id_checkout = request.POST.get('jadwal_id_checkout')
        status_checkin = request.POST.get('status_checkin')
        status_checkout = request.POST.get('status_checkout')
        laporan_checkin = request.FILES.get('laporan_checkin')
        laporan_checkout = request.FILES.get('laporan_checkout')
        type_absen = request.POST.get('type_absen')

        

        if type_absen == 'checkin':

            if jadwal_id_checkin:
                try:
                    jadwal_absensi = JadwalAbsensi.objects.get(
                        id=jadwal_id_checkin)
                    RekapAbsen.objects.create(
                        data_mahasiswa=request.user,
                        jadwal_absensi=jadwal_absensi,
                        status_absensi=status_checkin,
                        laporan=laporan_checkin,
                        waktu_absensi=now,
                        type_absensi = type_absen

                    )
                    # Ganti 'success_page' dengan nama URL tujuan setelah berhasil menyimpan
                    messages.success(request,'Sukses Check-in')
                    return redirect('absensi')
                except JadwalAbsensi.DoesNotExist:
                    # Tangani kasus jika jadwal_absensi tidak ditemukan
                    print("JadwalAbsensi not found")

        else:
            if jadwal_id_checkout:
                try:
                    jadwal_absensi = JadwalAbsensi.objects.get(
                        id=jadwal_id_checkout)
                    RekapAbsen.objects.create(
                        data_mahasiswa=request.user,
                        jadwal_absensi=jadwal_absensi,
                        status_absensi=status_checkout,
                        laporan=laporan_checkout,
                        waktu_absensi=now,
                        type_absensi = type_absen
                    )
                    # Ganti 'success_page' dengan nama URL tujuan setelah berhasil menyimpan
                    messages.success(request, 'Sukses Check-out')
                    return redirect('absensi')
                except JadwalAbsensi.DoesNotExist:
                    # Tangani kasus jika jadwal_absensi tidak ditemukan
                    print("JadwalAbsensi not found")

    context = {
        'judul': 'Halaman Absensi',
        'jadwal': jadwal_list,
        'now': now,
        'tanggal': today
    }
    return render(request, 'absensi.html', context)


@ijinkan_pengguna(yang_diizinkan=['peserta'])
@login_required(login_url='loginPage')
def sertifikat(request):
    peserta = request.user.peserta

    # Pastikan peserta sudah check-in dan check-out dengan status "hadir"
    checkin = RekapAbsen.objects.filter(
        data_mahasiswa=peserta.user, type_absensi='checkin', status_absensi='hadir').exists()
    checkout = RekapAbsen.objects.filter(
        data_mahasiswa=peserta.user, type_absensi='checkout', status_absensi='hadir').exists()

    if checkin and checkout:
        sertifikat_path = generate_certificate_pdf(peserta)
        context = {
            'judul': 'Halaman Sertifikat',
            'sertifikat_url': sertifikat_path.replace(settings.MEDIA_ROOT, settings.MEDIA_URL)
        }
    else:
        context = {
            'judul': 'Halaman Sertifikat',
            'error': 'Anda belum memenuhi syarat untuk mendapatkan sertifikat.'
        }

    return render(request, 'sertifikat.html', context)
