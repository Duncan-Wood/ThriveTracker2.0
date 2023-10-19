from django.urls import path
from . import views

urlpatterns = [
    path('introduction/', views.introduction, name='introduction'),
    path('lets-start-personalizing/', views.lets_start_personalizing, name='lets-start-personalizing'),
]
