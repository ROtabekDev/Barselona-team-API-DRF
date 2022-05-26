from turtle import title
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Players
from .serializers import PlayersSerializer

class PlayersAPIView(APIView):
    def get(self, request):
        lst = Players.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Players.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})


# class PlayersAPIView(generics.ListAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer

    
