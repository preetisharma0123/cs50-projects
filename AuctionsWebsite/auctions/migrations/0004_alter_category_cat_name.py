# Generated by Django 5.0.2 on 2024-04-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_remove_auction_listing_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]