# Generated by Django 4.1.1 on 2022-11-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_student_en_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='st_no',
            field=models.IntegerField(default=0),
        ),
    ]
