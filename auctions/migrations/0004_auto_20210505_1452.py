# Generated by Django 3.2 on 2021-05-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listings_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='listings',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='listings',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]