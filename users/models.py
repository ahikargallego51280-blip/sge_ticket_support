from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username