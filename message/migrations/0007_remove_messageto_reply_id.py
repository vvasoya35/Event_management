# Generated by Django 4.1 on 2022-10-25 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0006_remove_messageto_reply_messageto_reply_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageto',
            name='reply_id',
        ),
    ]
