# Generated by Django 2.2.7 on 2019-11-28 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypodcasts', '0012_auto_20191128_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='category',
        ),
    ]