# Generated by Django 3.2.7 on 2021-11-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0050_alter_biodata_partner_financial_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='bondha_partner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='bondha',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
