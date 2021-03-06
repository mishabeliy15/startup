# Generated by Django 2.2 on 2019-06-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypodcasts', '0008_episode_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='link_apple',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='link_google',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='link_spotify',
            field=models.URLField(blank=True),
        ),
    ]
