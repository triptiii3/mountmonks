# Generated by Django 4.0.6 on 2022-08-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_image', models.CharField(max_length=200)),
                ('destination_title', models.CharField(max_length=100)),
                ('inner_video', models.CharField(max_length=500)),
                ('inner_details', models.CharField(max_length=100)),
                ('inner_title', models.CharField(max_length=50)),
            ],
        ),
    ]
