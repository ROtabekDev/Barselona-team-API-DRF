from django.shortcuts import render
from rest_framework import generics
from .models import Players
from .serializers import PlayersSerializer

class PlayersAPIView(generics.ListAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer

    
