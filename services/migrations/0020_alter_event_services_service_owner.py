# Generated by Django 4.1 on 2022-11-03 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_profiles_profile'),
        ('services', '0019_alter_booking_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_services',
            name='service_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
