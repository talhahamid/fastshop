# Generated by Django 4.1.7 on 2024-01-31 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0003_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='forwhom',
            field=models.CharField(default='null', max_length=30),
        ),
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
