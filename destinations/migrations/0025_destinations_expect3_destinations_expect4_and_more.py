# Generated by Django 4.0.6 on 2022-09-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0024_alter_destinations_daycontent1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinations',
            name='expect3',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='destinations',
            name='expect4',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='destinations',
            name='expect5',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]
