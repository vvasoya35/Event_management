# Generated by Django 4.1 on 2022-09-02 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_event_services_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_services',
            name='category',
        ),
        migrations.AddField(
            model_name='event_services',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service_category'),
        ),
    ]
