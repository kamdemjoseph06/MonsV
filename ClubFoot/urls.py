from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Inscription ,name="inscription"),
    path('', views.Connexion ,name="connexion"),
    path('', views.Evenement ,name="evenement"),
]
