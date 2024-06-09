from django import forms
from django.forms import ModelForm
from .models import Peserta

class FormPeserta(ModelForm):
    # JENIS_KELAMIN_CHOICES = [
    #     ('L', 'Laki-laki'),
    #     ('P', 'Perempuan')
    # ]
    
    # STATUS_MAHASISWA_CHOICES = [
    #     ('baru', 'Baru'),
    #     ('lama', 'Lama'),
        
    # ]
    
    # FAKULTAS_CHOICES = [
    #     ('fakultas teknik', 'Fakultas Teknik'),
    #     ('fakultas soshum', 'Fakultas Soshum'),
    #     ('fakultas pai', 'Fakultas Pai'),
    #     ('fakultas kesehatan', 'Fakultas Kesehatan'),

    #     # Add more fakultas choices here
    # ]
    
    # PRODI_CHOICES = [
    #     ('prodi1', 'Prodi 1'),
    #     ('prodi2', 'Prodi 2'),
    #     # Add more prodi choices here
    # ]
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