# Generated by Django 2.2.7 on 2019-11-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantryapp', '0011_auto_20191119_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='name',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
