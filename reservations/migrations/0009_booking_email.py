# Generated by Django 4.2.23 on 2025-06-29 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_remove_booking_email_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
