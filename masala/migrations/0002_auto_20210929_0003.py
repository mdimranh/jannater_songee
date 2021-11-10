# Generated by Django 3.2.7 on 2021-09-28 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='masala_catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='masala',
            name='writter',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='masala',
            name='catagory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='masala.masala_catagory'),
        ),
    ]