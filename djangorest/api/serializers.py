from rest_framework import serializers
from .models import *

class YambScoresSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format"""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Game
        fields = ('id', 'player1_name', 'player1_score', 'player2_name', 'player2_score')
        # read_only_fields = ('date_created', 'date_modified')
