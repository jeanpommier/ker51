# Generated by Django 3.2.5 on 2021-08-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hivernants', '0002_alter_email_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='email'),
        ),
    ]
