# Generated by Django 4.1.2 on 2022-11-04 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0007_remove_seleksi_tanggal_mulai_ujian_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='program_studi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='Program Studi+', to='admission.seleksi'),
        ),
    ]
