# Generated by Django 3.0.5 on 2020-07-14 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_postview_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postview',
            name='view_count',
        ),
    ]
