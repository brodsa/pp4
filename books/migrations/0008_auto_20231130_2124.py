# Generated by Django 3.2.22 on 2023-11-30 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_bookcontribution_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookcontribution',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='bookcontribution',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='unique_user_book_contribution'),
        ),
    ]