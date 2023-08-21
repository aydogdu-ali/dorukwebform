from django.db import models

# Create your models here.

class FormData(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=20)
    phonenumber = models.IntegerField()
    email = models.EmailField()
    mesaj = models.TextField()

    def __str__(self):
        return self.firstname