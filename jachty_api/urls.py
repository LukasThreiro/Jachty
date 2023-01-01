#from django.conf.urls import url
from django.urls import path, include
from .views import (
    TypyJachtowApiView,
    JachtyZagloweApiView,
    JachtyMotoroweApiView,
    WolneDniView,
    JachtyZaglowe
)

urlpatterns = [
    path("typy_jachtow", TypyJachtowApiView.as_view()),
    path("jachty/zaglowe", JachtyZagloweApiView.as_view()),
    path("jachty/motorowe", JachtyMotoroweApiView.as_view()),
    path("terminy", WolneDniView.as_view()),
    path("jachty/zaglowe2", JachtyZaglowe)
]