# Generated by Django 4.1.1 on 2024-01-17 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_room', '0011_alter_message_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 17, 18, 45, 42, 177118, tzinfo=datetime.timezone.utc)),
        ),
    ]