# Generated by Django 4.1.1 on 2022-11-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_studentresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='en_no',
            field=models.IntegerField(default=0),
        ),
    ]
