
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Players
from .serializers import PlayersSerializer

class PlayersAPIView(APIView):
   
    def get(self, request):
        p = Players.objects.all().values()
        return Response({'posts': PlayersSerializer(p, many=True).data})


    def post(self, request):
        serializer = PlayersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        post_new = Players.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': PlayersSerializer(post_new).data})


# class PlayersAPIView(generics.ListAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer

    
