# Generated by Django 5.2 on 2025-04-16 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_product_options_alter_variation_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='typej',
            new_name='type',
        ),
    ]
