from dataclasses import fields
from rest_framework import serializers
from .models import Players


class PlayersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Players
        fields = ('title', 'cat_id')