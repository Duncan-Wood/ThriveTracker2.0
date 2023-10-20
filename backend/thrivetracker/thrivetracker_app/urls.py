from django.urls import path
from . import views

urlpatterns = [
    path('introduction/', views.introduction, name='introduction'),
    path('lets-start-personalizing/', views.lets_start_personalizing, name='lets-start-personalizing'),
    path('weekly-drink-count/', views.weekly_drink_count, name='weekly-drink-count'),

]
