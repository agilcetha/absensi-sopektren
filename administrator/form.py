from django import forms
from django.forms import ModelForm
from .models import Peserta, JadwalAbsensi

class FormPeserta(ModelForm):
    class Meta:
        model = Peserta
        fields = ['nama_mahasiswa',
                  'nomor_induk_mahasiswa',
                  'jenis_kelamin',
                  'status_mahasiswa',
                  'alamat',
                  'nomor_telepon',
                  'fakultas',
                  'prodi'
                  ]
        widgets = {
            'nama_mahasiswa': forms.TextInput(attrs={'class': 'form-control'}),
            'nomor_induk_mahasiswa': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
            'status_mahasiswa': forms.Select(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'nomor_telepon': forms.TextInput(attrs={'class': 'form-control'}),
            'fakultas': forms.Select(attrs={'class': 'form-control'}),
            'prodi': forms.Select(attrs={'class': 'form-control'})
        }

        labels ={
            'nama_mahasiswa':'Nama Mahasiswa',
            'nomor_induk_mahasiswa': 'Nim',
            'jenis_kelamin': 'Jenis Kelamin',
            'status_mahasiwa': 'Status ',
            'alamat': 'Alamat',
            'nomor_telepon': 'No Telepon',
            'fakultas': 'Fakultas',
            'prodi': 'Prodi'
        }


class FormBerandaPeserta(ModelForm):
    class Meta:
        model = Peserta
        fields = ['nama_mahasiswa',
                  'nomor_induk_mahasiswa',
                  'jenis_kelamin',
                  'status_mahasiswa',
                  'alamat',
                  'nomor_telepon',
                  'fakultas',
                  'prodi'
                  ]
        widgets = {
            'nama_mahasiswa': forms.TextInput(attrs={'class': 'form-control'}),
            'nomor_induk_mahasiswa': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
            'status_mahasiswa': forms.Select(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'nomor_telepon': forms.TextInput(attrs={'class': 'form-control'}),
            'fakultas': forms.Select(attrs={'class': 'form-control'}),
            'prodi': forms.Select(attrs={'class': 'form-control'})
        }

        labels ={
            'nama_mahasiswa':'Nama Mahasiswa',
            'nomor_induk_mahasiswa': 'Nim',
            'jenis_kelamin': 'Jenis Kelamin',
            'status_mahasiwa': 'Status ',
            'alamat': 'Alamat',
            'nomor_telepon': 'No Telepon',
            'fakultas': 'Fakultas',
            'prodi': 'Prodi'
        }


class FormJadwalAbsensi(ModelForm):
    class Meta:
        model = JadwalAbsensi
        fields = ['tanggal', 'checkin_mulai', 'checkin_selesai',
                  'checkout_mulai', 'checkout_selesai']
        widgets = {
            'tanggal': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Tanggal'}),
            'checkin_mulai': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'HH:MM'}),
            'checkin_selesai': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'HH:MM'}),
            'checkout_mulai': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'HH:MM'}),
            'checkout_selesai': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'HH:MM'}),
        }
        labels = {
            'tanggal': 'Tanggal',
            'checkin_mulai': 'Checkin Mulai',
            'checkin_selesai': 'Checkin Selesai',
            'checkout_mulai': 'Checkout Mulai',
            'checkout_selesai': 'Checkout Selesai'
        }
