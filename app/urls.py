from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api_01/', views.api_01, name='api_01'),
    path('index3/', views.index3, name='index3'),
]
