# Generated by Django 4.1.1 on 2024-01-17 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_room', '0008_alter_message_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['msg_time']},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='timestamp',
            new_name='msg_time',
        ),
    ]
