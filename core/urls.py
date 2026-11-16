from django.urls import path

from core import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('panel/', views.dashboard, name='dashboard'),
]
