from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
    path("physical-attributes/", views.save_physical_attributes, name="physical-attributes"),
    path("get-physical-attributes/", views.get_users_physical_attributes, name="physical-attributes"),
]