from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from pharmacy.models import Warehouse


class AnimalSpecies(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AnimalBreed(models.Model):
    name = models.CharField(max_length=50)
    species = models.ForeignKey(AnimalSpecies, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AnimalShelter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    warehouse = models.ForeignKey(
        Warehouse,
        blank=True,
        null=True,
        on_delete=models.RESTRICT,
        related_name="warehouse_for_shelter",
    )

    def __str__(self):
        return self.name


class Animal(models.Model):
    id_number = models.CharField(max_length=50)
    species = models.ForeignKey(
        AnimalSpecies, blank=True, null=True, on_delete=models.RESTRICT
    )
    breed = models.ForeignKey(
        AnimalBreed, blank=True, null=True, on_delete=models.RESTRICT
    )
    shelter = models.ForeignKey(
        AnimalShelter, blank=True, null=True, on_delete=models.RESTRICT
    )
    age = models.IntegerField()
    arrival_date = models.DateTimeField(default=now)
    surrender_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    owner = models.CharField(max_length=100, null=True, blank=True)
    owner_address = models.TextField(null=True, blank=True)
    owner_phone = models.CharField(max_length=15, null=True, blank=True)
    owner_email = models.EmailField(null=True, blank=True)
    behavior_pattern = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="animals/")

    created_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="created_animals_user"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="updated_animals_user"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_number


class AnimalTransaction(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.RESTRICT, related_name="animal")
    from_shelter = models.ForeignKey(
        AnimalShelter,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="from_shelter",
    )
    to_shelter = models.ForeignKey(
        AnimalShelter,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="to_shelter",
    )
    created_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="created_animal_transaction_user"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="updated_animal_transaction_user"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
