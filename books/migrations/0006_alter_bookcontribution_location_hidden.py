# Generated by Django 3.2.22 on 2023-11-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_bookcontribution_location_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcontribution',
            name='location_hidden',
            field=models.TextField(blank=True, null=True),
        ),
    ]