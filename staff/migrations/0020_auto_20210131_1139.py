# Generated by Django 3.1.4 on 2021-01-31 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0019_auto_20210124_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='branch',
            field=models.CharField(choices=[('Computer Engineering', 'Computer Engineering'), ('Information Technology', 'Information Technology')], max_length=70, verbose_name='Branch'),
        ),
    ]
