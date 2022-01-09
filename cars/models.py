from django.db import models
from django.contrib.auth.models import User
from cars.views import get_brands


class Client(models.Model):
    firstname = models.CharField(max_length=32, verbose_name="Imię", null=True, blank=True)
    lastname = models.CharField(max_length=32, verbose_name="Nazwisko", null=True, blank=True)
    phone = models.CharField(max_length=16, verbose_name="Numer telefonu", null=True, blank=True)
    email = models.CharField(max_length=64, verbose_name="Email", null=True, blank=True)

    class Meta:
        verbose_name = "klient"
        verbose_name_plural = 'Klienci'

    def __str__(self):
        return "{} {} (tel: {} )".format(self.firstname, self.lastname, self.phone)


class Car(models.Model):
    FUEL = {
        (0, 'Benzyna'),
        (1, 'Benzyna+CNG'),
        (2, 'Benzyna+LPG'),
        (3, 'Diesel'),
        (4, 'Elektryczny'),
        (5, 'Etanol'),
        (6, 'Hybryda'),
        (7, 'Wodór'),
    }

    car_brand = models.CharField(max_length=32, verbose_name="Marka", null=True, blank=True)
    brand_model = models.CharField(max_length=32, blank=True, verbose_name="Model", null=True)
    year = models.PositiveSmallIntegerField(default=2000, verbose_name="Rocznik", null=True, blank=True)
    registration_number = models.CharField(max_length=12, unique=False, verbose_name="Numer rejestracyjny",
                                           null=True, blank=True)
    vin = models.CharField(max_length=24, default='', unique=False, verbose_name="Numer VIN", null=True, blank=True)
    engine_capacity = models.CharField(max_length=24, default='', verbose_name="Pojemnośc silnika", null=True,
                                       blank=True)
    power = models.CharField(max_length=10, verbose_name="Moc (kW)", null=True, blank=True)
    car_mileage = models.IntegerField(null=True, blank=True, verbose_name="Przebieg")
    fuel_type = models.PositiveSmallIntegerField(default=0, verbose_name="Rodzaj paliwa", choices=FUEL)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Właściciel")

    class Meta:
        verbose_name = "samochód"
        verbose_name_plural = 'Samochody'

    def __str__(self):
        return self.car_data()

    def car_data(self):
        return "{} {} ({}) {}".format(self.car_brand, self.brand_model, self.year, self.registration_number)


class Repair(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Samochód")
    start_date = models.DateField(null=True, blank=True, verbose_name="Data przyjęcia")
    end_date = models.DateField(null=True, blank=True, verbose_name="Data naprawy")
    description = models.TextField(default="", null=True, blank=True, verbose_name="Opis")
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Naprawiał")

    class Meta:
        verbose_name = "naprawa"
        verbose_name_plural = 'Naprawy'

    def __str__(self):
        return self.repair_data()

    def repair_data(self):
        return "{} data {}".format(self.car, str(self.end_date))
