from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Fakultas)
admin.site.register(Prodi)
admin.site.register(Peserta)
admin.site.register(JadwalAbsensi)
admin.site.register(RekapAbsen)
admin.site.register(SertifikatTemplate)



