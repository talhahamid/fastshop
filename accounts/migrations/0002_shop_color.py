# Generated by Django 4.1.7 on 2024-02-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='color',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
