# Generated by Django 5.0 on 2024-04-22 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingRatingStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_count', models.IntegerField(default=0)),
                ('rating_average', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('listing', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='listingRatingStats', to='api.listing')),
            ],
            options={
                'verbose_name': 'Listing Rating Stat',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_choices', models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')])),
                ('review', models.TextField(blank=True, null=True)),
                ('listing', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='listrating', to='api.listing')),
                ('profile_user', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to='api.profile')),
            ],
            options={
                'verbose_name': 'Make Rating',
                'unique_together': {('profile_user', 'listing')},
            },
        ),
    ]
