# Generated by Django 3.0.7 on 2020-10-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201021_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitedurl',
            name='url',
            field=models.URLField(max_length=1500),
        ),
    ]