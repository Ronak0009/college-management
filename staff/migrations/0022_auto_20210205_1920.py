# Generated by Django 3.1.4 on 2021-02-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0021_merge_20210205_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='branch',
            field=models.CharField(choices=[('Computer Engineering', 'Computer Engineering'), ('Information Technology', 'Information Technology'), ('Electronics and Comm. Engineering', 'Electronics and Comm. Engineering'), ('Bio-Medical Engineering', 'Bio-Medical Engineering'), ('Mechantronics Engineering', 'Mechantronics Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Marine Engineering', 'Marine Engineering'), ('Automobile Engineering', 'Automobile Engineering'), ('Petrochemical Engineering', 'Petrochemical Engineering')], max_length=70, verbose_name='Branch'),
        ),
    ]