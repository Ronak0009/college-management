# Generated by Django 3.1.4 on 2021-01-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=70)),
                ('username', models.CharField(max_length=70)),
                ('passwd', models.CharField(max_length=70)),
                ('confirm_passwd', models.CharField(max_length=70)),
                ('enrollment', models.CharField(max_length=70)),
                ('date', models.CharField(max_length=70)),
                ('mobile', models.CharField(max_length=10)),
                ('college', models.CharField(choices=[('Uvpce', 'U.V Patel College of Engineering'), ('Bspp', 'B.S Patel Polytechnic')], max_length=70)),
                ('branch', models.CharField(choices=[('Ce', 'Computer Engineering'), ('It', 'Information Technology ')], max_length=70)),
                ('sem', models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III')], max_length=5)),
                ('email', models.EmailField(max_length=70)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=7)),
            ],
        ),
    ]