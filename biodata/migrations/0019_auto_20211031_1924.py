# Generated by Django 3.2.7 on 2021-10-31 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0018_auto_20211031_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='family_haram_income',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biodata',
            name='haram_income',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]