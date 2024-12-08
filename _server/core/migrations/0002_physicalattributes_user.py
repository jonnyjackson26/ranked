# Generated by Django 5.0.3 on 2024-12-07 23:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='physicalattributes',
            name='user',
            field=models.OneToOneField(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='physical_attributes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
