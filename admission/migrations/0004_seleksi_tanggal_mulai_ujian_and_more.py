# Generated by Django 4.1.2 on 2022-11-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_remove_admission_jalur'),
    ]

    operations = [
        migrations.AddField(
            model_name='seleksi',
            name='tanggal_mulai_ujian',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='seleksi',
            name='tanggal_selesai_ujian',
            field=models.DateField(null=True),
        ),
    ]
