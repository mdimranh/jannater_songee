# Generated by Django 3.2.7 on 2021-10-31 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0017_auto_20211026_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='job_permission',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='study_permission',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='takecare_porda',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]