# Generated by Django 4.0.6 on 2022-08-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_leh_lehtrip'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadtours',
            name='mode',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roadtours',
            name='mode_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
