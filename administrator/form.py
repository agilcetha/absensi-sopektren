from django import forms
from django.forms import ModelForm
from .models import Peserta, JadwalAbsensi
from django.core.exceptions import ValidationError

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
            'na hasiswa':'Nama Mahasiswa',
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


class FormRegister(ModelForm):
    class Meta:
        model = Peserta
        fields = [
            'nama_mahasiswa',
            'nomor_induk_mahasiswa',
            'jenis_kelamin',
            'status_mahasiswa',
            'alamat',
            'nomor_telepon',
            'fakultas',
            'prodi',
            'password',
            'konfirmasi_password',
            'upload_registrasi'
        ]
        widgets = {
            'nama_mahasiswa': forms.TextInput(attrs={'class': 'form-control'}),
            'nomor_induk_mahasiswa': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
            'status_mahasiswa': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'nomor_telepon': forms.TextInput(attrs={'class': 'form-control'}),
            'fakultas': forms.Select(attrs={'class': 'form-control'}),
            'prodi': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'konfirmasi_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'upload_registrasi': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nama_mahasiswa': 'Nama Mahasiswa',
            'nomor_induk_mahasiswa': 'NIM',
            'jenis_kelamin': 'Jenis Kelamin',
            'status_mahasiswa': 'Status Mahasiswa',
            'alamat': 'Alamat',
            'nomor_telepon': 'No Telepon',
            'fakultas': 'Fakultas',
            'prodi': 'Prodi',
            'password': 'Password',
            'konfirmasi_password': 'Konfirmasi Password',
            'upload_registrasi': 'Bukti Registrasi (*.jpg/*.png)'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status_mahasiswa'].initial = 'Belum'  # Nilai default
        # Set field as read-only
        self.fields['status_mahasiswa'].widget.attrs['readonly'] = True
        # Optional: Add some CSS to make the read-only field look visually different
        self.fields['status_mahasiswa'].widget.attrs['style'] = 'pointer-events: none; background-color: #e9ecef;'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError(
                'Password harus memiliki minimal 8 karakter.')
        return password
