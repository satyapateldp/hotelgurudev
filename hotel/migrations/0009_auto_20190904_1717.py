# Generated by Django 2.2.3 on 2019-09-04 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='email',
            new_name='useremail',
        ),
    ]
