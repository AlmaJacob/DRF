from rest_framework import serializers
from .models import *


#normal serializers
class Sample(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()
    place=serializers.CharField()

#modal serializers
class model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Project_user
        fields='__all__'
