# Generated by Django 2.2.7 on 2019-11-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypodcasts', '0010_podcast_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='categories',
            field=models.ManyToManyField(default=[], to='category.SubCategory'),
        ),
    ]
