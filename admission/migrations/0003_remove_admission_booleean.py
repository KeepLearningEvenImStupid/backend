# Generated by Django 4.1.2 on 2022-10-18 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_admission_booleean'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='booleean',
        ),
    ]