# Generated by Django 2.2.1 on 2019-08-24 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor_app', '0013_donor_is_contact_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='blood_price_per_100gramm',
        ),
    ]
