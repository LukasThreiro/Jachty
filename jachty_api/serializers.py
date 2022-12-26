from rest_framework import serializers
from .models import TypJachtu, Jacht, Klient, Rezerwacja

class TypJachtuSerializer(serializers.ModelSerializer):
	class Meta:
		model = TypJachtu
		fields = ["IDTypu", "nazwaTypu"]

class JachtSerializer(serializers.ModelSerializer):
	class Meta:
		model = Jacht
		fields = ["IDJachtu", "IDTypu", "nazwa", "cenaZaDobe", "zdjecie", "opis"]

class KlientSerializer(serializers.ModelSerializer):
	model = Klient
	fields = ["IDKlienta", "imie", "nazwisko", "pesel"]

class RezerwacjaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rezerwacja
		fields = ["IDRezerwacji", "IDJachtu", "IDKlienta", "dataOd", "dataDo", "uwagi"]