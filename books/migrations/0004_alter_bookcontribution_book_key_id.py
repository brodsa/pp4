# Generated by Django 3.2.22 on 2023-11-27 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_bookcontribution_book_key_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcontribution',
            name='book_key_id',
            field=models.IntegerField(),
        ),
    ]