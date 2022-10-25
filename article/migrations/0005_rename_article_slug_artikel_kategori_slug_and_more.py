# Generated by Django 4.1.2 on 2022-10-25 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_artikel_article_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='article_slug',
            new_name='kategori_slug',
        ),
        migrations.AlterField(
            model_name='artikel',
            name='kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='article.kategori'),
        ),
    ]