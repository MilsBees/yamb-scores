from rest_framework import generics
from .serializers import YambScoresSerializer
from .models import *

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of the API."""
    queryset = Game.objects.all()
    serializer_class = YambScoresSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new yamb score."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Game.objects.all()
    serializer_class = YambScoresSerializer