# Generated by Django 4.2.3 on 2023-07-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dissemination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today', models.DateTimeField(auto_now_add=True)),
                ('firstNameEN', models.CharField(blank=True, max_length=255)),
                ('surNameEN', models.CharField(blank=True, max_length=255)),
                ('phoneNrEN', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('Latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=10)),
                ('Longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=10)),
                ('orgEN', models.CharField(blank=True, max_length=255)),
                ('partner', models.CharField(blank=True, max_length=255)),
                ('event', models.CharField(blank=True, max_length=255)),
                ('title', models.TextField(blank=True)),
                ('startdate', models.DateField()),
                ('participant_list', models.BooleanField(default=False)),
                ('farmers_M', models.IntegerField(default=0)),
            ],
        ),
    ]
