# Generated by Django 2.2.7 on 2019-11-29 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20191129_0028'),
        ('mypodcasts', '0014_remove_podcast_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='languages.Language'),
        ),
    ]
