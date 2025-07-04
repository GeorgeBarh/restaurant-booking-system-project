# Generated by Django 4.2.23 on 2025-06-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_alter_menuitem_options_alter_table_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='image',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='status',
            field=models.IntegerField(choices=[(0, 'Unavailable'), (1, 'Available')], default=1),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
