# Generated by Django 4.0.6 on 2022-08-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_backpack_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backpack',
            old_name='inner_title',
            new_name='batch1',
        ),
        migrations.RenameField(
            model_name='bikingtours',
            old_name='inner_title',
            new_name='batch1',
        ),
        migrations.RenameField(
            model_name='lehtrip',
            old_name='inner_title',
            new_name='batch1',
        ),
        migrations.RenameField(
            model_name='spiti',
            old_name='inner_title',
            new_name='batch1',
        ),
        migrations.RenameField(
            model_name='weekend',
            old_name='inner_title',
            new_name='batch1',
        ),
        migrations.RemoveField(
            model_name='backpack',
            name='inner_details',
        ),
        migrations.RemoveField(
            model_name='bikingtours',
            name='destination_title',
        ),
        migrations.RemoveField(
            model_name='bikingtours',
            name='inner_details',
        ),
        migrations.RemoveField(
            model_name='lehtrip',
            name='inner_details',
        ),
        migrations.RemoveField(
            model_name='populartours',
            name='destination_title',
        ),
        migrations.RemoveField(
            model_name='recenttours',
            name='destination_title',
        ),
        migrations.RemoveField(
            model_name='roadtours',
            name='inner_details',
        ),
        migrations.RemoveField(
            model_name='roadtours',
            name='inner_title',
        ),
        migrations.RemoveField(
            model_name='spiti',
            name='inner_details',
        ),
        migrations.RemoveField(
            model_name='weekend',
            name='inner_details',
        ),
        migrations.AddField(
            model_name='backpack',
            name='batch2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backpack',
            name='batch3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backpack',
            name='batch4',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backpack',
            name='batch5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='backpack',
            name='batch6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='backpack',
            name='batch7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode1_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode2_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode3_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode4_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='backpack',
            name='mode5_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='batch2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='batch3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='batch4',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='batch5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='batch6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='batch7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode1_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode2_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode3_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode4_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bikingtours',
            name='mode5_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='batch2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='batch3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='batch4',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='batch5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='batch6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='batch7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode1_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode2_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode3_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode4_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lehtrip',
            name='mode5_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='populartours',
            name='batch1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='batch2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='batch3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='batch4',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='batch5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='populartours',
            name='batch6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='populartours',
            name='batch7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='populartours',
            name='inner_video',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode1_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode2_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode3_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode4_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='populartours',
            name='mode5_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recenttours',
            name='batch1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='batch2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='batch3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='batch4',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='batch5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recenttours',
            name='batch6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recenttours',
            name='batch7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recenttours',
            name='inner_video',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode1_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode2_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode3_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode4_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recenttours',
            name='mode5_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='spiti',
            name='batch2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spiti',
            name='batch3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spiti',
            name='batch4',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spiti',
            name='batch5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='spiti',
            name='batch6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='spiti',
            name='batch7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode1_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode2_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode3_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode4_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='spiti',
            name='mode5_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='batch2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekend',
            name='batch3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekend',
            name='batch4',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekend',
            name='batch5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='batch6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='batch7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode1_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode2_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode3_price',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode4_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='weekend',
            name='mode5_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bikingtours',
            name='id',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='populartours',
            name='id',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recenttours',
            name='id',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode1_price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode2_price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode3',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode3_price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode4_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='roadtours',
            name='mode5_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
