# Generated by Django 2.2.7 on 2019-11-29 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
