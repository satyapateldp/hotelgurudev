# Generated by Django 2.2.3 on 2019-09-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20190902_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='roomcharge',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]