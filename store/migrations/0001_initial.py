# Generated by Django 4.2 on 2023-05-13 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path_cat)),
                ('descrption', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1 = hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1 = Trending')),
                ('meta_tilte', models.CharField(max_length=150)),
                ('meta_keyword', models.CharField(max_length=150)),
                ('meta_description', models.CharField(max_length=150)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path_prodcut)),
                ('descrption', models.TextField(max_length=500)),
                ('small_descrption', models.TextField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=default, 1 = hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1 = Trending')),
                ('tags', models.CharField(blank=True, max_length=150, null=True)),
                ('meta_tilte', models.CharField(max_length=150)),
                ('meta_keyword', models.CharField(max_length=150)),
                ('meta_description', models.CharField(max_length=150)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('poruduct_qty', models.IntegerField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('prouduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
