# Generated by Django 4.2.7 on 2023-11-11 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_carmodel_car_price_alter_carmodel_car_year'),
        ('posts', '0005_remove_userpostsmodel_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpostsmodel',
            name='car',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='cars.carmodel'),
            preserve_default=False,
        ),
    ]
