# Generated by Django 3.2.13 on 2022-09-28 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_products_image', models.ImageField(blank=True, upload_to='media')),
                ('products_image1', models.ImageField(blank=True, upload_to='media')),
                ('products_image2', models.ImageField(blank=True, upload_to='media')),
                ('products_image3', models.ImageField(blank=True, upload_to='media')),
                ('product_title', models.CharField(max_length=200)),
                ('product_desc', models.CharField(max_length=600)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MainProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_image', models.ImageField(upload_to='media')),
                ('products_video', models.FileField(blank=True, upload_to='media/%y')),
                ('product_title', models.CharField(max_length=200)),
                ('product_desc', models.CharField(max_length=600)),
                ('product_spec1', models.CharField(max_length=600)),
                ('product_spec2', models.CharField(max_length=600)),
                ('product_spec3', models.CharField(max_length=600)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('expected_delivery_date', models.DateTimeField()),
                ('complete', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, max_length=100)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer')),
            ],
            options={
                'ordering': ['customer'],
            },
        ),
    ]
