# Generated by Django 3.2.5 on 2021-07-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0009_auto_20210730_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='emails',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='phones',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]