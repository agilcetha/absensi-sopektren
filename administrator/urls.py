from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.beranda_admin, name='beranda_admin'),
    path('data_peserta/', views.data_peserta, name='data_peserta'),
    path('jadwal_absensi/', views.jadwal_absen, name='jadwal_absensi'),
    path('rekap_absen/', views.rekap_absen, name='rekap_absen'),
    path('tambah_peserta/', views.tambah_peserta, name='tambah_peserta'),
    path('edit_peserta/<str:pk>', views.edit_peserta, name='edit_peserta'),
    path('hapus_peserta/<str:pk>', views.hapus_peserta, name='hapus_peserta'),
    path('data_fakultas/', views.data_fakultas, name='data_fakultas'),
    path('konfirmasi/<str:pk>', views.konfirmasi, name='konfirmasi'),
    path('batal/<str:pk>', views.batal, name='batal'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)