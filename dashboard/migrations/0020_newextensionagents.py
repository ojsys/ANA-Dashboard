# Generated by Django 4.2.3 on 2024-02-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_alter_farmers_own_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewExtensionAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('phone_no', models.CharField(max_length=100, null=True)),
                ('phone_no2', models.CharField(max_length=100, null=True)),
                ('whatsapp', models.BooleanField(default=False, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('education', models.CharField(choices=[('Secondary', 'Secondary'), ('Diploma', 'Diploma'), ('Degree', 'Degree'), ('Masters', 'Masters'), ('PhD', 'PhD')], max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('type_org', models.CharField(choices=[('NGO', 'NGO'), ('Government', 'Government'), ('Private', 'Private')], max_length=100, null=True)),
                ('org', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
