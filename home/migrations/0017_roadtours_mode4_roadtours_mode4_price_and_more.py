# Generated by Django 4.0.6 on 2022-08-28 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_rename_mode_roadtours_mode1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadtours',
            name='mode4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='roadtours',
            name='mode4_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='roadtours',
            name='mode5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='roadtours',
            name='mode5_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
