# Generated by Django 3.1.6 on 2021-04-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='Age',
        ),
        migrations.AddField(
            model_name='client',
            name='Date',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
    ]
