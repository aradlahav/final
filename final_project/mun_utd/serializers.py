from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['number', 'first_name', 'last_name', 'nationality',
                  'hire_date', 'position', 'second_position', 'salary',
                  'max_bonus', 'picture']
