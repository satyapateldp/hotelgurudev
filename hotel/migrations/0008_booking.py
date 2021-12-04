# Generated by Django 2.2.3 on 2019-09-04 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20190904_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.CharField(choices=[('maharaja suite', 'maharaja suite'), ('Suite', 'Suite'), ('Super Deluxe', 'Super Deluxe'), ('A.C. Deluxe', 'A.C. Deluxe'), ('Premium Rooms', 'Premium Rooms')], max_length=20)),
                ('roomtype', models.CharField(choices=[('single', 'single'), ('double', 'double')], max_length=10)),
                ('dateofstay', models.DateField()),
                ('numberofroom', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.userreg')),
            ],
        ),
    ]