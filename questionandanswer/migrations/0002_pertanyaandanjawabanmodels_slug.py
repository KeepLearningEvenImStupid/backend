# Generated by Django 4.1.2 on 2022-10-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pertanyaandanjawabanmodels',
            name='slug',
            field=models.SlugField(default='Belum Diisi', max_length=255),
        ),
    ]
