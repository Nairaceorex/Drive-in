# Generated by Django 3.1.6 on 2021-03-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0003_auto_20210306_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='Icon',
            field=models.ImageField(upload_to='', verbose_name='Иконка'),
        ),
    ]
