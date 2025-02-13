# Generated by Django 4.0.6 on 2022-09-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_recenttours_reltourimg1_recenttours_reltourimg2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekend',
            name='relatedit1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='relatedit2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='relatedprice1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='relatedprice2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='relatedtour1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='relatedtour2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='reltourimg1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='weekend',
            name='reltourimg2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
