from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    id_number = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    owner = models.CharField(max_length=100, null=True, blank=True)
    owner_address = models.TextField(null=True, blank=True)
    owner_phone = models.CharField(max_length=15, null=True, blank=True)
    owner_email = models.EmailField(null=True, blank=True)
    behavior_pattern = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="created_animals_user"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="updated_animals_user"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
