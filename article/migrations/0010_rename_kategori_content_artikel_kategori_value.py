# Generated by Django 4.1.2 on 2022-10-25 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_artikel_kategori_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='kategori_content',
            new_name='kategori_value',
        ),
    ]
