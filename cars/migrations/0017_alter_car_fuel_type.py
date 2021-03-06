# Generated by Django 4.0 on 2021-12-31 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_alter_car_fuel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Benzyna+LPG'), (6, 'Hybryda'), (0, 'Benzyna'), (5, 'Etanol'), (1, 'Benzyna+CNG'), (4, 'Elektryczny'), (7, 'Wodór'), (3, 'Diesel')], default=0, verbose_name='Rodzaj paliwa'),
        ),
    ]
