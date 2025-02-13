# Generated by Django 4.0.6 on 2022-08-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0011_alter_manali_daycontent1_alter_manali_daycontent2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manali',
            name='daycontent1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='daycontent2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='daycontent3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='daycontent4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='dayno2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='dayno3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='dayno4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='destination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='difficulty',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='group',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='hiketype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='itineraryhead1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='itineraryhead2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='itineraryhead3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='itineraryhead4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='minage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='pickup',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manali',
            name='time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
