# Generated by Django 3.2.22 on 2023-12-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='likes',
        ),
        migrations.AlterField(
            model_name='bookcontribution',
            name='location',
            field=models.CharField(choices=[('by a friend', 'by a friend '), ('at a hidden place', 'at a hidden place'), ('it is my book', 'it is my book')], max_length=20),
        ),
    ]