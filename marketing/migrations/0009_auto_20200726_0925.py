# Generated by Django 3.0.8 on 2020-07-26 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0008_delete_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='msg',
        ),
    ]
