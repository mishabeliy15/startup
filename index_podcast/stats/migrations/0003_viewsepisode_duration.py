# Generated by Django 2.2.7 on 2019-11-29 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20191129_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewsepisode',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]