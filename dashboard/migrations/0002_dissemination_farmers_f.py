# Generated by Django 4.2.3 on 2023-07-24 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dissemination',
            name='farmers_F',
            field=models.IntegerField(default=0),
        ),
    ]
