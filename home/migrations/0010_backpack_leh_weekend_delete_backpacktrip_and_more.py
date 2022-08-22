# Generated by Django 4.0.6 on 2022-08-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_spiti_delete_spititrip'),
    ]

    operations = [
        migrations.CreateModel(
            name='backpack',
            fields=[
                ('id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('destination_title', models.CharField(max_length=100)),
                ('destination_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('inner_video', models.CharField(max_length=500)),
                ('inner_details', models.CharField(max_length=100)),
                ('inner_title', models.CharField(max_length=50)),
                ('destination_price', models.CharField(max_length=50)),
                ('old_price', models.CharField(max_length=50)),
                ('new_price', models.CharField(max_length=50)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('hiketype', models.CharField(blank=True, max_length=50, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=50, null=True)),
                ('pickup', models.CharField(blank=True, max_length=50, null=True)),
                ('minage', models.CharField(blank=True, max_length=50, null=True)),
                ('dayno1', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead1', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent1', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno2', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead2', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent2', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno3', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead3', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent3', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno4', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead4', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent4', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno5', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead5', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent5', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno6', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead6', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent6', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno7', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead7', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent7', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno8', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead8', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent8', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno9', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead9', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent9', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno10', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead10', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent10', models.CharField(blank=True, max_length=200, null=True)),
                ('meetingpoint', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('expect1', models.CharField(blank=True, max_length=400, null=True)),
                ('expect2', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='leh',
            fields=[
                ('id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('destination_title', models.CharField(max_length=100)),
                ('destination_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('inner_video', models.CharField(max_length=500)),
                ('inner_details', models.CharField(max_length=100)),
                ('inner_title', models.CharField(max_length=50)),
                ('destination_price', models.CharField(max_length=50)),
                ('old_price', models.CharField(max_length=50)),
                ('new_price', models.CharField(max_length=50)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('hiketype', models.CharField(blank=True, max_length=50, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=50, null=True)),
                ('pickup', models.CharField(blank=True, max_length=50, null=True)),
                ('minage', models.CharField(blank=True, max_length=50, null=True)),
                ('dayno1', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead1', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent1', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno2', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead2', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent2', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno3', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead3', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent3', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno4', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead4', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent4', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno5', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead5', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent5', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno6', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead6', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent6', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno7', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead7', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent7', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno8', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead8', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent8', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno9', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead9', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent9', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno10', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead10', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent10', models.CharField(blank=True, max_length=200, null=True)),
                ('meetingpoint', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('expect1', models.CharField(blank=True, max_length=400, null=True)),
                ('expect2', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='weekend',
            fields=[
                ('id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('destination_title', models.CharField(max_length=100)),
                ('destination_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('inner_video', models.CharField(max_length=500)),
                ('inner_details', models.CharField(max_length=100)),
                ('inner_title', models.CharField(max_length=50)),
                ('destination_price', models.CharField(max_length=50)),
                ('old_price', models.CharField(max_length=50)),
                ('new_price', models.CharField(max_length=50)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination_image6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('hiketype', models.CharField(blank=True, max_length=50, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=50, null=True)),
                ('pickup', models.CharField(blank=True, max_length=50, null=True)),
                ('minage', models.CharField(blank=True, max_length=50, null=True)),
                ('dayno1', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead1', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent1', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno2', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead2', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent2', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno3', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead3', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent3', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno4', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead4', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent4', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno5', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead5', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent5', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno6', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead6', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent6', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno7', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead7', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent7', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno8', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead8', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent8', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno9', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead9', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent9', models.CharField(blank=True, max_length=200, null=True)),
                ('dayno10', models.CharField(blank=True, max_length=50, null=True)),
                ('itineraryhead10', models.CharField(blank=True, max_length=50, null=True)),
                ('daycontent10', models.CharField(blank=True, max_length=200, null=True)),
                ('meetingpoint', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('inclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions1', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions2', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions3', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions4', models.CharField(blank=True, max_length=50, null=True)),
                ('exclusions5', models.CharField(blank=True, max_length=50, null=True)),
                ('expect1', models.CharField(blank=True, max_length=400, null=True)),
                ('expect2', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='backpacktrip',
        ),
        migrations.DeleteModel(
            name='lehtrip',
        ),
        migrations.DeleteModel(
            name='weekendtrip',
        ),
    ]
