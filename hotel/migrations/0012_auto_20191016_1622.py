# Generated by Django 2.2.3 on 2019-10-16 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_auto_20191015_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='roomname',
            field=models.CharField(choices=[('Maharaja Suite', 'Maharaja Suite'), ('Suite', 'Suite'), ('Super Deluxe', 'Super Deluxe'), ('A.C. Deluxe', 'A.C. Deluxe'), ('Premium Rooms', 'Premium Rooms')], max_length=20),
        ),
    ]
