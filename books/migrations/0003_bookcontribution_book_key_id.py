# Generated by Django 3.2.22 on 2023-11-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_bookcontribution_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcontribution',
            name='book_key_id',
            field=models.IntegerField(default=9999),
        ),
    ]