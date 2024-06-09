from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Fakultas(models.Model):
    nama_fakultas = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nama_fakultas
    class Meta:
        verbose_name_plural = "Fakultas"

class Prodi(models.Model):
    nama_prodi = models.CharField(max_length=100)
    fakultas = models.ForeignKey(Fakultas, on_delete=models.CASCADE, related_name='prodi')

    def __str__(self):
        return f"{self.nama_prodi} ({self.fakultas.nama_fakultas})"
    class Meta:
        verbose_name_plural = "Prodi"

class Peserta(models.Model):
    JK=(
        ('Laki-Laki','Laki-Laki'),
        ('Perempuan','Perempuan')
    )
    STATUS =(
        ('Baru','Baru'),
        ('Lama','Lama')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama_mahasiswa = models.CharField(max_length=100)
    nomor_induk_mahasiswa = models.CharField(max_length=20, unique=True)
    jenis_kelamin = models.CharField(max_length=200, null=True,choices=JK)
    status_mahasiswa = models.CharField(max_length=200, null=True,choices=STATUS)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)
    fakultas = models.ForeignKey(Fakultas, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    prodi = models.ForeignKey(Prodi, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    


    def __str__(self):
        return f"{self.nama_mahasiswa} ({self.nomor_induk_mahasiswa})"
    class Meta:
        verbose_name_plural = "Data Peserta"
