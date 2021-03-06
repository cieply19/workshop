# Generated by Django 4.0 on 2021-12-30 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imię', models.CharField(max_length=32)),
                ('Nazwisko', models.CharField(max_length=32)),
                ('Numer telefonu', models.CharField(max_length=16)),
                ('Email', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marka', models.CharField(max_length=32)),
                ('Model', models.CharField(max_length=32)),
                ('Rocznik', models.PositiveSmallIntegerField(default=2000)),
                ('Numer rejestracyjny', models.CharField(default='', max_length=12)),
                ('Numer VIN', models.CharField(default='', max_length=24, unique=True)),
                ('Pojemnośc silnika', models.CharField(default='', max_length=24)),
                ('power', models.CharField(default='', max_length=24)),
                ('car_mileage', models.IntegerField(blank=True, null=True)),
                ('fuel_type', models.CharField(default='', max_length=24)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.client')),
            ],
        ),
    ]
