# Generated by Django 2.0.6 on 2018-11-26 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=50),
        ),
    ]