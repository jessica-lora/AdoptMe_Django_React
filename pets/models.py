from django.db import models

# Create your models here.

class Pets(models.Model):
    
    animals = [("DOG", "Dog"), 
               ("CAT", "Cat"), 
               ("RODENT", "Rodent"), 
               ("BIRD", "Bird"), 
               ("REPTILE", "Reptile")]
    
    image = models.ImageField(upload_to="pets/", default="default/defaultdog.jpg")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=None)
    animal = models.CharField(max_length=100, choices=animals)
    breed = models.CharField(max_length=100, default="Unknown")
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    intake = models.DateTimeField(auto_now_add=True)

