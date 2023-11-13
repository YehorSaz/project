# Generated by Django 4.2.7 on 2023-11-10 20:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPostsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('region', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('views_count', models.IntegerField(default=0)),
                ('update_count', models.IntegerField(default=0)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='cars.carmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'posts',
                'ordering': ['id'],
            },
        ),
    ]
