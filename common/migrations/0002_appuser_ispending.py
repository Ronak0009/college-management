# Generated by Django 3.1.4 on 2021-01-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='isPending',
            field=models.BooleanField(default=True, max_length=10),
        ),
    ]
