# Generated by Django 3.1.6 on 2021-03-02 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('Key_Film', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Код фильма')),
                ('Name', models.CharField(max_length=100, verbose_name='Название')),
                ('Year', models.IntegerField(verbose_name='Год')),
                ('Description', models.TextField(verbose_name='Описание')),
                ('Genre', models.CharField(max_length=50, verbose_name='Жанр')),
            ],
        ),
    ]