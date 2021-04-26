from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_show', views.add_show),
]
