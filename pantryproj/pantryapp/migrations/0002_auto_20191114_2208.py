# Generated by Django 2.2.7 on 2019-11-14 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pantryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_data',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_name',
            new_name='name',
        ),
    ]
