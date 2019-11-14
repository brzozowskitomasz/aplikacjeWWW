from django.db import models

class wypozyczenia(models.Model):
    data_wypozycz = models.DateTimeField('data wypozyczenia')
    data_oddania = models.DateTimeField('data oddania')

class kategorie(models.Model):
    nazwa = models.CharField(max_length=45)

class wydawnictwo(models.Model):
    nazwa = models.CharField(max_length=45)

class autorzy(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)

class ksiazki(models.Model):
    tytul = models.CharField(max_length=45)
    opis = models.CharField(max_length=45)
    rok_wydania = models.DateTimeField('rok wydania')

class czytelnicy(models.Model):
    login = models.CharField(max_length=45)
    haslo = models.CharField(max_length=45)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    data_urodzenia = models.DateTimeField('data urodzenia')
    nr_telefonu = models.CharField(max_length=45)

# Create your models here.
