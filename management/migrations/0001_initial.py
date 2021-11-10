# Generated by Django 3.2.7 on 2021-11-08 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('send_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('seen', models.BooleanField(default=False)),
                ('action', models.CharField(choices=[('no', 'no'), ('progress', 'progress'), ('done', 'done')], default='no', max_length=250)),
            ],
        ),
    ]
