# Generated by Django 4.2.3 on 2023-11-03 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='phone_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
