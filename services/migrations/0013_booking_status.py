# Generated by Django 4.1 on 2022-10-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Running', 'Running'), ('Completed', 'Completed')], default='Processing', max_length=200),
        ),
    ]
