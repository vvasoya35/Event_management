# Generated by Django 4.1 on 2022-11-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_remove_booking_end_time_remove_booking_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]