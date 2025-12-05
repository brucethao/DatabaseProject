from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    is_zookeeper = models.BooleanField(default = False)

class Location(models.Model):
    continent = models.CharField(max_length = 100)
    habitat = models.CharField(max_length = 100, unique = True)
#unique shouldn't be the key if there is an idea also having uniqueness
#prevents proper data to be stored (Ex. Continent: "North America" Habitat: "Wetlands")
# & Continent: "North America" Habitat: "Wetlands") can't be stored together)

class Classification(models.Model):
    type = models.CharField(max_length = 100)

class Animal(models.Model):
    name = models.CharField(max_length = 100)
    species = models.CharField(max_length=100)
    age = models.IntegerField(default = 0)
    weight = models.DecimalField(max_digits = 5, decimal_places = 2)
    classification = models.ForeignKey(Classification, on_delete = models.CASCADE)
    animal_habitat = models.ForeignKey(Location, on_delete = models.CASCADE)
#Cannot add more than 3 digits before decimal point.

class Zookeeper(models.Model):
    wage = models.DecimalField(max_digits = 5, decimal_places = 2)
    hours = models.DecimalField(max_digits = 5, decimal_places = 2)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

class Food(models.Model):
    food_name = models.CharField(max_length = 100)

class Diet(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    food_name = models.ForeignKey(Food, on_delete = models.CASCADE)

class AnimalFeedingLog(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    food_name = models.ForeignKey(Food, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 5, decimal_places = 2)
    last_fed = models.DateTimeField(auto_now_add = True)
    zookeeper = models.ForeignKey(Zookeeper, on_delete = models.CASCADE)
# to do
class Medication(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    medication_name = models.CharField(max_length = 100)
    medication_amount = models.DecimalField(max_digits = 5, decimal_places = 2)

class FunFact(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    bio = models.CharField(max_length = 100)
    fun_facts = models.CharField(max_length = 100)
    #Varchar length should be increased for descriptions.

class AnimalMedicationLog(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

class Show(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    ticket_price = models.DecimalField(max_digits = 5, decimal_places = 2)
    location = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)

class Product(models.Model):
    item_name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)