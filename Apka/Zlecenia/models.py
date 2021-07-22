from django.db import models

class Zlecenie(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    czas = models.IntegerField("Liczba dni przeznaczona na zlecenie:",)
    def __str__(self):
        return self.nazwa

class Pracownik(models.Model):
    pass

class Dykrektor(models.Model):
    pass