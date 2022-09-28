from django.urls import path

from . import views

app_name = 'cliente'
urlpatterns = [
<<<<<<< HEAD
    path('', views.IndexView.as_view(), name='index'),
    # nuevas vistas
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/resultado/', views.ResultadoView.as_view(), name='resultado'),
    # path('<String:apellido>/resultado', views.resultado, name='resultado'),
]
=======
    path('', views.index, name='index'),
]
>>>>>>> parent of 0a3799a (Modelos de clases para base de datos)
