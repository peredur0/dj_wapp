from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Band(models.Model):
    
    class Genre(models.TextChoices):
        METAL = 'M'
        ROCK = 'R'
        SOUL = 'S'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
            validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Listing(models.Model):

    class Categorie(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True)
    categorie = models.fields.CharField(choices=Categorie.choices, max_length=5)

    def __str__(self):
        return self.title



