# Generated by Django 4.2.1 on 2023-05-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloc', '0002_finance_actif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
