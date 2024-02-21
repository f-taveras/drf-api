# Generated by Django 5.0.2 on 2024-02-21 04:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0002_rename_planets_planet'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='code',
            new_name='planet',
        ),
        migrations.AlterField(
            model_name='planet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planets', to=settings.AUTH_USER_MODEL),
        ),
    ]
