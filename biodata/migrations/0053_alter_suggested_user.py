# Generated by Django 3.2.7 on 2021-11-22 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0052_remove_biodata_divorced_houseband'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggested',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bio', to='biodata.biodata'),
        ),
    ]
