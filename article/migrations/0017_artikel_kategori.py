# Generated by Django 4.1.2 on 2022-10-26 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_remove_artikel_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.kategori'),
        ),
    ]
