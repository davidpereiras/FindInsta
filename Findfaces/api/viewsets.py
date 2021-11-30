from rest_framework import viewsets
from Findfaces.api import serializers
from Findfaces import models 

class FindfacesViewset(viewsets.ModelViewSet):
 serializer_class = serializers.FindFaceSerializer
 queryset = models.img.objects.all()