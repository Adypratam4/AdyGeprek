# Generated by Django 4.2.7 on 2023-12-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suradi', '0003_produk_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='banner_dua',
            field=models.ImageField(null=True, upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)'),
        ),
    ]
