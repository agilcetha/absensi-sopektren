from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.beranda_peserta, name='beranda_peserta'),
    path('absensi/', views.absensi, name='absensi'),
    path('sertifikat/', views.sertifikat, name='sertifikat'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
