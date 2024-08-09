# Generated by Django 3.2.12 on 2024-08-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0016_auto_20240729_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sertifikat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('template_file', models.FileField(upload_to='sertifikat/templates/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
