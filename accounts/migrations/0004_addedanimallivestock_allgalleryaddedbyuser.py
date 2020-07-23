# Generated by Django 3.0.8 on 2020-07-22 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_pricefilter_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_userprofileinfo_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddedAnimalLiveStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_tag', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(auto_now_add=True)),
                ('animal_breed', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=1000, null=True)),
                ('male_parent', models.CharField(blank=True, max_length=100, null=True)),
                ('female_parent', models.CharField(blank=True, max_length=100, null=True)),
                ('animal_type', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_img/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_admin_verified', models.BooleanField(default=False)),
                ('is_call_verified', models.BooleanField(default=False)),
                ('category_instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animal_add', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animal_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AllGalleryAddedByUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.AddedAnimalLiveStock')),
            ],
        ),
    ]