# Generated by Django 2.2.7 on 2019-11-15 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pantryapp', '0007_auto_20191115_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='name',
            field=models.CharField(default='name', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
