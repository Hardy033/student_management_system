# Generated by Django 4.1.1 on 2022-11-06 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_attendance_attendance_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendace_date',
            new_name='attendance_date',
        ),
    ]