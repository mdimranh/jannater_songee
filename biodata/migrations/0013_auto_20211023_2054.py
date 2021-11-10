# Generated by Django 3.2.7 on 2021-10-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0012_alter_biodata_daora_hadith_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='blood_group',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='brother',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='children',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='graduate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='know_family',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='sister',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='ssc_pass_year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='ssc_result',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]