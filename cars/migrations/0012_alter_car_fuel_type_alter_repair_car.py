# Generated by Django 4.0 on 2021-12-31 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_car_fuel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Etanol'), (2, 'Benzyna+LPG'), (3, 'Elektryczny'), (1, 'Benzyna+CNG'), (3, 'Wodór'), (3, 'Hybryda'), (0, 'Benzyna'), (3, 'Diesel')], default=0, verbose_name='Rodzaj paliwa'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.car', verbose_name='Samochód'),
        ),
    ]
