# Generated by Django 2.2.7 on 2019-11-15 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pantryapp', '0005_ingredient_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]