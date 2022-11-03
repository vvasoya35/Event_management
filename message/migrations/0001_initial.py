# Generated by Django 3.2.7 on 2022-10-11 05:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0011_review_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='messageTo',
            fields=[
                ('message', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.event_services')),
            ],
        ),
    ]
