import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


from .models import Players
   

class PlayersModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ("title", "content", "cat")
 


# def encode():
#     model = PlayersModel('Eldor Shomurodov', 'Content: UZB N1')
#     model_sr = PlayersSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def  decode():
#     stream = io.BytesIO(b'{"title": "Odil Axmedov", "content":"Content: Uzbekistan FA"}')
#     data = JSONParser().parse(stream)
#     serializer = PlayersSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)