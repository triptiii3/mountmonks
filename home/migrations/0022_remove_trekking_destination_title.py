# Generated by Django 4.0.6 on 2022-08-28 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_rename_inner_title_backpack_batch1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trekking',
            name='destination_title',
        ),
    ]
