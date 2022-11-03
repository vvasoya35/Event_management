# Generated by Django 4.1 on 2022-11-03 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_profiles_profile'),
        ('services', '0018_booking_end_time_booking_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Accept', 'Accept'), ('Running', 'Running'), ('Completed', 'Completed')], default='Processing', max_length=200),
        ),
        migrations.AlterField(
            model_name='event_services',
            name='service_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
