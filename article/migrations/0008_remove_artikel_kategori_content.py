# Generated by Django 4.1.2 on 2022-10-25 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_artikel_kategori_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikel',
            name='kategori_content',
        ),
    ]
