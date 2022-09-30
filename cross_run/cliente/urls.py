from django.urls import path

from . import views

app_name = 'cliente'
urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.IndexView.as_view(), name='index'),
    # nuevas vistas
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/resultado/', views.ResultadoView.as_view(), name='resultado'),
    # path('<String:apellido>/resultado', views.resultado, name='resultado'),
]

    

