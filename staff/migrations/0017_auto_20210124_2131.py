# Generated by Django 3.1.4 on 2021-01-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0016_auto_20210124_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='branch',
            field=models.CharField(choices=[('Purvesh', 'Purvesh'), ('Ronak', 'Ronak'), ('Purvesh', 'Purvesh'), ('Purvesh', 'Purvesh'), ('NewB', 'NewB')], max_length=70, verbose_name='Branch'),
        ),
    ]
