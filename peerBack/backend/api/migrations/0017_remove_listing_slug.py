# Generated by Django 5.0.3 on 2024-05-03 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0016_remove_listing_user_profile_listing_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listing",
            name="slug",
        ),
    ]
