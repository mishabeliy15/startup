# Generated by Django 2.2 on 2019-06-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypodcasts', '0006_auto_20190620_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='category',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]