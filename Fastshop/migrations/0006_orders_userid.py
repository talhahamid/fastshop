# Generated by Django 4.1.7 on 2024-02-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fastshop', '0005_orders_customercontact_orders_ownercontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='userid',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]