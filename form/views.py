from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import FormData
from .serializer import FormDataSerializers

from rest_framework.response import Response #mail için
from django.core.mail import send_mail #mail için



class FormDataMVS(ModelViewSet):
    queryset= FormData.objects.all()
    serializer_class= FormDataSerializers



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Form verilerini al
        firstname = serializer.validated_data.get('firstname')
        lastname = serializer.validated_data.get('lastname')
        phonenumber = serializer.validated_data.get('phonenumber')
        email = serializer.validated_data.get('email')
        mesaj = serializer.validated_data.get('mesaj')

        # E-posta gönderme işlemi
        send_mail(
            'Doruk Dijital Ajans Webden Gelen',
            f'Ad: {firstname}\nSoyad: {lastname}\nTelefon: {phonenumber}\nE-posta: {email}\nMesaj: {mesaj}',
            'your_email@gmail.com',  # Gönderici e-posta adresi
            ['dorukdijitalajans@gmail.com'],  # Hedef e-posta adresi
            fail_silently=False,
        )

       