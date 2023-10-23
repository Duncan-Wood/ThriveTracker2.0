""" URL Configuration for thrivetracker_app """""
from django.urls import path
from . import views

urlpatterns = [
    path('introduction/', views.introduction, name='introduction'),
    path('lets-start-personalizing/', views.lets_start_personalizing,
         name='lets-start-personalizing'),
    path('weekly-drink-count/', views.weekly_drink_count,
         name='weekly-drink-count'),
    path('typical-week/', views.typical_week,
         name='typical-week'),
    path('drink-recommendation/', views.drink_recommendation,
         name='drink-recommendation'),
]
