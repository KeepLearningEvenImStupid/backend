# Generated by Django 4.1.2 on 2022-10-25 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_rename_article_slug_artikel_kategori_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='artikel_slug',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
