# Generated by Django 4.2 on 2023-05-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.URLField(default='https://shopeyblack.com/'),
            preserve_default=False,
        ),
    ]
