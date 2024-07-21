from django.urls import path
from  . import views

urlpatterns = [
    path('corusel', views.corusel, name='form'),
    path('test/<int:id>/', views.test, name='test'),
]