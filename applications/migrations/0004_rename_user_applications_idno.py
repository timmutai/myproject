# Generated by Django 4.0.1 on 2022-06-24 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_rename_sponsorshipstatus_applications_sponsorshipapproval_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='user',
            new_name='idno',
        ),
    ]
