# Generated by Django 3.1.6 on 2021-03-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_film_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='Icon',
            field=models.ImageField(upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
