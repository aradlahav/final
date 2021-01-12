from django.urls import path, include
from . import views
from rest_framework import routers
routers = routers.DefaultRouter()
routers.register('Player', views.PlayerView)
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('json', include(routers.urls)),
    path('<slug:slug>/', views.player_page, name='item')
]
