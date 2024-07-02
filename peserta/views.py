from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from dashboard.decorators import ijinkan_pengguna
from administrator.form import FormBerandaPeserta
from administrator.models import Peserta
from django.http import HttpResponse




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