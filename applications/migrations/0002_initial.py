# Generated by Django 4.0.1 on 2022-06-20 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='idno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
