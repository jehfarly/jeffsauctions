# Generated by Django 3.2 on 2021-05-25 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_listings_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='listings_won', to=settings.AUTH_USER_MODEL),
        ),
    ]
