# Generated by Django 4.2.3 on 2023-11-03 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_alter_farmers_farm_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmers',
            name='farm_area',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
    ]