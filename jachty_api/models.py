from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices

class TypJachtu(models.Model):
	TYPY = Choices(
		"żaglowy",
		"motorowy"
	)

	IDTypu = models.IntegerField(primary_key=True, unique=True)
	nazwaTypu = models.CharField(max_length=64, choices=TYPY)

class Jacht(models.Model):
	IDJachtu = models.IntegerField(primary_key=True, unique=True)
	IDTypu = models.ForeignKey(TypJachtu, on_delete=models.CASCADE)
	nazwa = models.CharField(max_length=128)
	cenaZaDobe = models.FloatField()
	zdjecie = models.CharField(max_length=256)
	opis = models.CharField(max_length=2048)

class Klient(models.Model):
	IDKlienta = models.IntegerField(primary_key=True, unique=True)
	imie = models.CharField(max_length=64)
	nazwisko = models.CharField(max_length=64)
	pesel = models.CharField(max_length=11)

class Rezerwacja(models.Model):
	IDRezerwacji = models.IntegerField(primary_key=True, unique=True)
	IDJachtu = models.ForeignKey(Jacht, on_delete=models.CASCADE)
	IDKlienta = models.ForeignKey(Klient, on_delete=models.CASCADE)
	dataOd = models.DateTimeField(auto_now=False)
	dataDo = models.DateTimeField(auto_now=False)
	uwagi = models.CharField(max_length=2048)
