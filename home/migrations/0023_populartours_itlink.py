# Generated by Django 4.0.6 on 2022-08-29 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_trekking_destination_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='populartours',
            name='itlink',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
