from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, timedelta, datetime
from django.http import HttpResponse, JsonResponse
from asgiref.sync import sync_to_async

from .models import TypJachtu, Jacht, Klient, Rezerwacja
from .serializers import JachtSerializer, TypJachtuSerializer

from django.http import HttpResponse

class JachtyZagloweApiView(APIView):
	#@sync_to_async
	def post(self, request, *args, **kwargs):
		jachty = Jacht.objects.filter(IDTypu = 1)
		serializer = JachtSerializer(jachty, many=True)
		resp = {"data": serializer.data}
		return Response(resp, status=status.HTTP_200_OK)
	
	#@sync_to_async
	def get(self, request, *args, **kwargs):
		jachty = Jacht.objects.filter(IDTypu = 1)
		serializer = JachtSerializer(jachty, many=True)
		return JsonResponse(serializer.data, safe=False)
		

@sync_to_async
def JachtyZaglowe(request):
	jachty = Jacht.objects.filter(IDTypu = 1)
	serializer = JachtSerializer(jachty, many=True)
	r = serializer.data
	resp = {"data": r}
	#return Response(resp, status=status.HTTP_200_OK)
	return HttpResponse(resp)

class JachtyMotoroweApiView(APIView):
	def post(self, request, *args, **kwargs):
		jachty = Jacht.objects.filter(IDTypu = 2)
		serializer = JachtSerializer(jachty, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class TypyJachtowApiView(APIView):
	def post(self, request, *args, **kwargs):
		typy_jachtow = TypJachtu.objects
		serializer = TypJachtuSerializer(typy_jachtow, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class WolneDniView(APIView):
	def daterange(self, start_date, end_date):
		for n in range(int((end_date - start_date).days) + 1):
			yield start_date + timedelta(n)

	def post(self, request, *args, **kwargs):
		# READING INPUT PARAMETERS
		try:
			_IDJachtu = request.data["IDJachtu"]
			_DataOd = request.data["DataOd"]
			_DataDo = request.data["DataDo"]
		except:
			return Response(
				{"res": "An error occurred while reading input parameters."}, 
				status=status.HTTP_400_BAD_REQUEST
			)

		# CHECKING DATA CORECTNESS
		j = Jacht.objects.filter(IDJachtu = _IDJachtu).count()

		if (j == 0):
			return Response(
				{"res": "ERROR. There is no yacht with the given ID."}, 
				status=status.HTTP_400_BAD_REQUEST
			)

		try:
			poczatek = datetime.strptime(_DataOd, "%Y-%m-%d")
		except:
			return Response(
				{"res": "ERROR. Invalid format DataOd. Correct format: YYYY-MM-DD."},
				status=status.HTTP_400_BAD_REQUEST
			)

		try:
			koniec = datetime.strptime(_DataDo, "%Y-%m-%d")
		except:
			return Response(
				{"res": "ERROR. Invalid format DataDo. Correct format: YYYY-MM-DD."},
				status=status.HTTP_400_BAD_REQUEST
			)

		# COMPUTING RESULTS
		rezerwacje = Rezerwacja.objects.filter(
			IDJachtu = _IDJachtu,
			dataOd__lte = _DataDo,
			dataDo__gte = _DataOd
		).order_by("dataOd")

		response = {}
		response["IDJachtu"] = _IDJachtu

		# Najpierw ustaw wszystkie jako wolne
		for single_date in self.daterange(poczatek, koniec):
			response[single_date.strftime("%Y-%m-%d")] = 0
		
		# Potem ustaw niektore jako zajete
		for r in rezerwacje:
			for single_date in self.daterange(r.dataOd, r.dataDo):
				if (single_date.strftime("%Y-%m-%d") in response):
					response[single_date.strftime("%Y-%m-%d")] = 1

		return Response(response)
