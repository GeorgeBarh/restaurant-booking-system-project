# Generated by Django 4.2.23 on 2025-06-29 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_booking_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='guests',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
