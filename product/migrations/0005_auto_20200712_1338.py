# Generated by Django 3.0.8 on 2020-07-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200712_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketAddByAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_name', models.CharField(blank=True, max_length=25, null=True)),
                ('market_image', models.FileField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('location', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='is_admin_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_call_verified',
            field=models.BooleanField(default=False),
        ),
    ]
