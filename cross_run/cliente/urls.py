from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # nuevas vistas de prueba
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/resultado/', views.resultado, name='resultado'),
    # path('<String:apellido>/resultado', views.resultado, name='resultado'),
]
