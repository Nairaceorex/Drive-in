# Generated by Django 3.1.6 on 2021-04-16 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0003_cinema_ticket'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Account',
        ),
    ]
