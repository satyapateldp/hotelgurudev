# Generated by Django 2.2.3 on 2019-08-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userfeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('dateofstay', models.DateField()),
                ('ratethehotel', models.CharField(max_length=20)),
                ('testimonial', models.CharField(max_length=400)),
            ],
        ),
    ]
