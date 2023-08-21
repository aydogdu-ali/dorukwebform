from rest_framework import serializers
from .models import FormData

class FormDataSerializers(serializers.ModelSerializer):
    
    class Meta:
        model= FormData
        fields= "__all__"