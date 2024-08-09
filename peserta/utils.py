import os
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import SertifikatTemplate
from django.utils import timezone
from administrator.models import *


def cek_kehadiran(peserta):
    checkin = RekapAbsen.objects.filter(
        data_mahasiswa=peserta.user, type_absensi='checkin', status_absensi='hadir').exists()
    checkout = RekapAbsen.objects.filter(
        data_mahasiswa=peserta.user, type_absensi='checkout', status_absensi='hadir').exists()
    return checkin and checkout


def generate_certificate_pdf(peserta):
    # Mengambil template sertifikat pertama, Anda bisa menyesuaikan ini
    template = SertifikatTemplate.objects.first()

    if not template or not template.template_file:
        raise ValueError("Template sertifikat tidak ditemukan")

    # Menentukan path untuk menyimpan PDF
    pdf_path = os.path.join(settings.MEDIA_ROOT,
                            f'sertifikat_{peserta.nomor_induk_mahasiswa}.pdf')

    # Membuat canvas PDF
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Menentukan jalur font
    font_path = os.path.join(settings.BASE_DIR, 'static/fonts/Arial.ttf')
    if not os.path.exists(font_path):
        raise ValueError("File font tidak ditemukan di path: " + font_path)

    # Mendaftarkan dan menggunakan font
    c.setFont('Helvetica', 12)
    c.setFont('Helvetica-Bold', 40)

    # Menambahkan teks ke PDF
    c.drawString(100, 700, f"{peserta.nama_mahasiswa}")
    c.drawString(100, 650, f"{peserta.nomor_induk_mahasiswa}")
    c.drawString(100, 600, f"Fakultas: {peserta.fakultas.nama_fakultas}")
    c.drawString(100, 550, f"Prodi: {peserta.prodi.nama_prodi}")
    c.drawString(100, 500, f"Tanggal Terbit: {SertifikatTemplate.upload_date}")

    # Menyelesaikan dan menyimpan PDF
    c.showPage()
    c.save()

    return pdf_path