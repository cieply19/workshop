# Generated by Django 4.0 on 2021-12-31 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_car_fuel_type_alter_repair_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Hybryda'), (3, 'Etanol'), (2, 'Benzyna+LPG'), (0, 'Benzyna'), (3, 'Wodór'), (1, 'Benzyna+CNG'), (3, 'Diesel'), (3, 'Elektryczny')], default=0, verbose_name='Rodzaj paliwa'),
        ),
    ]
