# Generated by Django 4.1.2 on 2022-10-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionandanswer', '0003_alter_pertanyaandanjawabanmodels_jawaban_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pertanyaandanjawabanmodels',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
