from rest_framework import generics
from .serializers import VoteSerializer
from .models import Vote

class VoteViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

# Create your views here.
