from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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
        return f"{self.nama_prodi}"
    class Meta:
        verbose_name_plural = "Prodi"

class Peserta(models.Model):
    JK=(
        ('Laki-Laki','Laki-Laki'),
        ('Perempuan','Perempuan')
    )
    STATUS =(
        ('Belum','Belum'),
        ('Sudah','Sudah')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama_mahasiswa = models.CharField(max_length=100)
    nomor_induk_mahasiswa = models.CharField(max_length=20, unique=True)
    jenis_kelamin = models.CharField(max_length=200, null=True,choices=JK)
    status_mahasiswa = models.CharField(max_length=200, null=True,choices=STATUS)
    alamat = models.TextField(max_length=200)
    nomor_telepon = models.CharField(max_length=15)
    fakultas = models.ForeignKey(Fakultas, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    prodi = models.ForeignKey(Prodi, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    password = models.CharField(max_length=100, null=True)
    konfirmasi_password = models.CharField(max_length=100, null=True)
    upload_registrasi = models.ImageField(upload_to='photos/', null=True)
    

    def __str__(self):
        return f"{self.nama_mahasiswa} ({self.nomor_induk_mahasiswa})"
    class Meta:
        verbose_name_plural = "Data Peserta"


class JadwalAbsensi(models.Model):
    nama_kegiatan = models.CharField(max_length=100, null=True)
    tanggal = models.DateField()
    tahun_akademik = models.CharField(max_length=100, null=True)
    checkin_mulai = models.TimeField(default="00:00")
    checkin_selesai = models.TimeField(default="00:00")
    checkout_mulai = models.TimeField(default="00:00")
    checkout_selesai = models.TimeField(default="00:00")


    def __str__(self):
        return f"{self.tanggal} - Checkin: {self.checkin_mulai} - {self.checkin_selesai}, Checkout: {self.checkout_mulai} - {self.checkout_selesai}"
    class Meta:
        verbose_name_plural = "Jadwal Absensi"


class RekapAbsen(models.Model):
    data_mahasiswa = models.ForeignKey(User, on_delete=models.CASCADE)
    jadwal_absensi = models.ForeignKey(JadwalAbsensi, on_delete=models.CASCADE)
    status_absensi = models.CharField(max_length=100, choices=[('hadir', 'Hadir'), ('izin', 'Izin'), ('tidak_hadir', 'Tidak Hadir')])
    laporan = models.FileField(upload_to='laporan/', null=True, blank=True)
    waktu_absensi = models.DateTimeField(default=timezone.now)
    type_absensi = models.CharField(max_length=100, choices=[('checkin','Checkin'),('checkout','Checkout')], default='checkin')
    

    def __str__(self):
        return f"{self.data_mahasiswa}{self.jadwal_absensi}{self.status_absensi}{self.laporan}{self.waktu_absensi}{self.type_absensi}"
    class Meta:
        verbose_name_plural = "RekapAbsensi"
    


class SertifikatTemplate(models.Model):
    name = models.CharField(max_length=255)
    template_file = models.FileField(upload_to='sertifikat/templates/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}{self.upload_date}"
