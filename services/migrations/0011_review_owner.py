# Generated by Django 4.1 on 2022-09-17 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_profiles_profile'),
        ('services', '0010_event_services_service_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
