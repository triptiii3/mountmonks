# Generated by Django 4.0.6 on 2022-08-14 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0008_manali_day1_manali_daycontent2_manali_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manali',
            name='destination_image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='manali',
            name='destination_image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='manali',
            name='destination_image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='manali',
            name='destination_image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='manali',
            name='destination_image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='manali',
            name='destination_image6',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='manali',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
