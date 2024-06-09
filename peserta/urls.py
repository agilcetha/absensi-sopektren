from django.urls import path
from . import views 

urlpatterns = [
    path('', views.beranda_peserta, name='beranda_peserta'),
    path('absensi/', views.absensi, name='absensi'),
    path('sertifikat/', views.sertifikat, name='sertifikat'),

]