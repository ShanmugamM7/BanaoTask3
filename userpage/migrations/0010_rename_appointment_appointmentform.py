# Generated by Django 4.2.9 on 2024-02-20 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0009_appointment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appointment',
            new_name='AppointmentForm',
        ),
    ]
