
from rest_framework import generics
from .serializers import StuffedAnimalSerializer
from .models import StuffedAnimal
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class StuffedAnimalList(generics.ListCreateAPIView):
    queryset = StuffedAnimal.objects.all()
    serializer_class = StuffedAnimalSerializer


class StuffedAnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = StuffedAnimal.objects.all()
    serializer_class = StuffedAnimalSerializer