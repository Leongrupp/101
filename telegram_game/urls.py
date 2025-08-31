from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='telegram_game_index'),
]
