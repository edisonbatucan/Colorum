# Generated by Django 4.0.5 on 2022-06-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SUV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('num_seats', models.IntegerField()),
                ('wheel_size', models.CharField(max_length=50)),
            ],
        ),
    ]
