# Generated by Django 4.2 on 2023-05-15 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_poruduct_qty_card_porduct_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='porduct_qty',
            new_name='product_qty',
        ),
    ]
