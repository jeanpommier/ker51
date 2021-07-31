# Generated by Django 3.2.5 on 2021-07-29 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=200)),
                ('fulladdress', models.TextField(max_length=200)),
                ('phones', models.CharField(max_length=200)),
                ('emails', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]