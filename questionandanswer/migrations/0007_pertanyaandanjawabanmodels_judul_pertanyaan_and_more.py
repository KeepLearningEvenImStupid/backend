# Generated by Django 4.1.2 on 2022-10-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0006_pertanyaandanjawabanmodels_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pertanyaandanjawabanmodels',
            name='judul_pertanyaan',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='pertanyaandanjawabanmodels',
            name='no_hp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
