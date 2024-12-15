from django.contrib import admin

# Register your models here.

from .models import Fakultas, Prodi, Peserta,JadwalAbsensi

admin.site.register(Fakultas)
admin.site.register(Prodi)
admin.site.register(Peserta)
admin.site.register(JadwalAbsensi)

