# Generated by Django 3.2 on 2021-05-25 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_comments_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='my_comments', to='auctions.user'),
            preserve_default=False,
        ),
    ]
