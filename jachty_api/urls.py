#from django.conf.urls import url
from django.urls import path, include
from .views import (
    TypyJachtowApiView,
    JachtyApiView,
    WolneDniView
)

urlpatterns = [
    path("typy_jachtow", TypyJachtowApiView.as_view()),
    path("jachty", JachtyApiView.as_view()),
    path("terminy", WolneDniView.as_view()),
]