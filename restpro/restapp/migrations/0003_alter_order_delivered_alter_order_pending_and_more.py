# Generated by Django 4.1.4 on 2022-12-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_delete_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='pending',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_orders',
            field=models.IntegerField(max_length=30),
        ),
    ]
