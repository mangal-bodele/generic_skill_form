# Generated by Django 5.0.4 on 2024-04-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='duration',
            field=models.CharField(max_length=20),
        ),
    ]
