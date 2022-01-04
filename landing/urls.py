from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name="team"),
    path('terminos-y-condiciones/', views.tc, name="tc"),
    path('servicios/', views.services, name="services"),
]