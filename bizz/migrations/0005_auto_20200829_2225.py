# Generated by Django 3.0.9 on 2020-08-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizz', '0004_auto_20200828_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('on_market', 'On Market'), ('Sold', 'sold')], default='on_market', max_length=20),
        ),
    ]
