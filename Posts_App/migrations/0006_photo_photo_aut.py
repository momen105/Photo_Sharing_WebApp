# Generated by Django 3.2.6 on 2021-10-09 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Posts_App', '0005_auto_20211009_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo_aut',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo_aut', to=settings.AUTH_USER_MODEL),
        ),
    ]
