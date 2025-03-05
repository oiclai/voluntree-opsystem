from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('organization', 'Organization'),
        ('volunteer', 'Volunteer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='volunteer')

# Create your models here.
class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organization")
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="volunteer")
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
# faltando deixar view restrita