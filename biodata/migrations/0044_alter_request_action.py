# Generated by Django 3.2.7 on 2021-11-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0043_auto_20211116_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='action',
            field=models.CharField(blank=True, choices=[('send', 'send Request'), ('accept', 'accept Request'), ('reject', 'reject Request'), ('cancel', 'cancel Request'), ('married', 'married Request')], default=None, max_length=50, null=True),
        ),
    ]
