from django.urls import path
from . import views 

urlpatterns = [
    path('', views.beranda_admin, name='beranda_admin'),
    path('data_peserta/', views.data_peserta, name='data_peserta'),
    path('jadwal_absensi/', views.jadwal_absen, name='jadwal_absensi'),
    path('rekap_absen/', views.rekap_absen, name='rekap_absen'),
    path('tambah_peserta/', views.tambah_peserta, name='tambah_peserta'),
    path('edit_peserta/<str:pk>', views.edit_peserta, name='edit_peserta'),
    path('hapus_peserta/<str:pk>',views.hapus_peserta, name='hapus_peserta'),



]