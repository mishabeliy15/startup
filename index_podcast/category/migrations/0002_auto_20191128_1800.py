# Generated by Django 2.2.7 on 2019-11-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together={('category', 'name')},
        ),
    ]
