from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('verPost/<slug>', views.verPost),
    path('registrarPost/', views.registrarPost),
    path('edicionPost/<slug>', views.edicionPost),
    path('editarPost/', views.editarPost),
    path('eliminarPost/<slug>', views.eliminarPost)
]