# Generated by Django 2.2.7 on 2019-11-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('mypodcasts', '0009_auto_20190623_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='categories',
            field=models.ManyToManyField(to='category.SubCategory'),
        ),
    ]