# Generated by Django 4.1 on 2022-10-15 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_profiles_profile'),
        ('message', '0003_rename_service_messageto_mess_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageto',
            name='mess_receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='users.profile'),
        ),
        migrations.AddField(
            model_name='messageto',
            name='mess_sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
