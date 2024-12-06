from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
     path("physical-attributes/", views.physical_attributes, name="physical-attributes"),
]