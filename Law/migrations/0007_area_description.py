# Generated by Django 5.0.4 on 2025-03-26 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Law', '0006_member_statut'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='description',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
