from rest_framework import serializers
from Findfaces import models

class FindFaceSerializer(serializers.ModelSerializer):
 class Meta:
  model = models.img
  fields = '__all__'