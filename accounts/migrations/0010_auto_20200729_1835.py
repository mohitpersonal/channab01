# Generated by Django 3.0.8 on 2020-07-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_parentschild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addedanimallivestock',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='livestock_main_img/'),
        ),
        migrations.AlterField(
            model_name='allgalleryaddedbyuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery_livestock/'),
        ),
    ]
