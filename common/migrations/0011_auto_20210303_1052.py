# Generated by Django 3.1.4 on 2021-03-03 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_merge_20210205_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, default='', max_length=300, verbose_name='Description'),
        ),
    ]