# Generated by Django 4.1.2 on 2022-11-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0008_alter_admission_program_studi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seleksi',
            name='daya_tampung',
            field=models.BigIntegerField(blank=True),
        ),
    ]