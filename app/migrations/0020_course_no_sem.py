# Generated by Django 4.1.1 on 2022-12-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_staff_st_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='no_sem',
            field=models.IntegerField(default=6, max_length=10),
        ),
    ]