# Generated by Django 5.0.3 on 2024-05-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0030_listing_listing_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="Listing_Author",
            field=models.CharField(max_length=100),
        ),
    ]
