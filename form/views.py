from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import FormData
from .serializer import FormDataSerializers

# Create your views here.

class FormDataMVS(ModelViewSet):
    queryset= FormData.objects.all()
    serializer_class= FormDataSerializers



