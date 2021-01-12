from django.shortcuts import render, HttpResponse
from .models import Player
import mysql.connector
from rest_framework import viewsets, permissions
from .serializers import PlayerSerializer

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dont1know',
    database='players_db'
)

mycursor = mydb.cursor()


def homepage(request):
    players = Player.objects.all()
    return render(request, 'mun_utd/homepage.html', {'players': players})


class PlayerView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def player_page(request, slug):
    players = Player.objects.all()
    player = None
    for item in players:
        if item.slug == slug:
            player = item

    return render(request, 'mun_utd/player_page.html', {'player': player})
