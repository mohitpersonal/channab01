# Generated by Django 3.0.8 on 2020-08-01 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200801_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milklitre',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]