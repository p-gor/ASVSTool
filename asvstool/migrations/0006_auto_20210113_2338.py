# Generated by Django 3.1.5 on 2021-01-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asvstool', '0005_auto_20210113_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqsproject',
            name='result',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
