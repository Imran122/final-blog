# Generated by Django 3.0.5 on 2020-07-20 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_delete_softwarepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gadgetpost',
            name='maincategories',
        ),
        migrations.DeleteModel(
            name='MainCategorey',
        ),
    ]
