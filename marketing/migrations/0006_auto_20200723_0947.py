# Generated by Django 3.0.5 on 2020-07-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_auto_20200723_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]
