# Generated by Django 3.2.7 on 2021-10-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0014_alter_biodata_birth_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='hsc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='hsc_result',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='salat',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='ssc',
            field=models.CharField(max_length=100),
        ),
    ]
