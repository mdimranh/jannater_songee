# Generated by Django 3.2.7 on 2021-10-08 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0004_auto_20211007_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='publist',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
