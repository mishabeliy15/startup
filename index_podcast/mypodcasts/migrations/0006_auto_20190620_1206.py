# Generated by Django 2.2 on 2019-06-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypodcasts', '0005_podcast_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='explicit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='podcast',
            name='language',
            field=models.CharField(default='en', max_length=6),
        ),
    ]
