# Generated by Django 4.0.6 on 2022-10-03 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0006_alter_attendancereportstaff_attendance_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationstaffs',
            old_name='stafff_id',
            new_name='staff_id',
        ),
    ]
