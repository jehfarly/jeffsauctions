# Generated by Django 3.2 on 2021-05-06 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listings_starting_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='starting_bid',
        ),
    ]
