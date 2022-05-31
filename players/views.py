
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework import mixins
from rest_framework.decorators import action

from .models import Category, Players
from .serializers import PlayersSerializer


class PlayersViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    # queryset = Players.objects.all()
    serializer_class = PlayersSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Players.objects.all()[:3]

        return Players.objects.filter(pk=pk)

    @action(detail=True, methods=["get"])
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class PlayersAPIList(generics.ListCreateAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer


# class PlayersAPIUpdate(generics.UpdateAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer


# class PlayersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer


# class PlayersAPIView(APIView):
   
#     def get(self, request):
#         p = Players.objects.all()
#         return Response({'posts': PlayersSerializer(p, many=True).data})


#     def post(self, request):
#         serializer = PlayersSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Players.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         serializer = PlayersSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"post": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})

#         return Response({"post": "delete post" + str(pk)})

# class PlayersAPIView(generics.ListAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer

    
