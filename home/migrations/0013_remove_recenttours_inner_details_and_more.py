# Generated by Django 4.0.6 on 2022-08-22 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_populartours_inner_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recenttours',
            name='inner_details',
        ),
        migrations.RemoveField(
            model_name='recenttours',
            name='inner_title',
        ),
        migrations.RemoveField(
            model_name='recenttours',
            name='inner_video',
        ),
    ]
