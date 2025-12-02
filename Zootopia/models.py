from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    is_zookeeper = models.BooleanField(default = False)

class Location(models.Model):
    continent = models.CharField(max_length = 100)
    habitat = models.CharField(max_length = 100, unique = True)

class Classification(models.Model):
    type = models.CharField(max_length = 100)

class Animals(models.Model):
    name = models.CharField(max_length = 100)
    species = models.CharField(max_length=100)
    age = models.IntegerField(default = 0)
    weight = models.DecimalField(max_digits = 5, decimal_places = 2)
    classification = models.ForeignKey(Classification, on_delete = models.CASCADE)
    animal_habitat = models.ForeignKey(Location, on_delete = models.CASCADE)

class Zookeeper(models.Model):
    wage = models.DecimalField(max_digits = 5, decimal_places = 2)
    hours = models.DecimalField(max_digits = 5, decimal_places = 2)
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE)

class Foods(models.Model):
    food_name = models.CharField(max_length = 100)

class Diet(models.Model):
    animal = models.ForeignKey(Animals, on_delete = models.CASCADE)
    food_name = models.ForeignKey(Foods, on_delete = models.CASCADE)

class AnimalFeedingLog(models.Model):
    animal = models.ForeignKey(Animals, on_delete = models.CASCADE)
    food_name = models.ForeignKey(Foods, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 5, decimal_places = 2)
    last_fed = models.DateTimeField(auto_now_add = True)
    zookeeper = models.ForeignKey(Zookeeper, on_delete = models.CASCADE)
# to do
class Medication(models.Model):
    animal = models.ForeignKey(Animals, on_delete = models.CASCADE)
    medication_name = models.CharField(max_length = 100)
    medication_amount = models.DecimalField(max_digits = 5, decimal_places = 2)

class FunFacts(models.Model):
    animal = models.ForeignKey(Animals, on_delete = models.CASCADE)
    bio = models.CharField(max_length = 100)
    fun_facts = models.CharField(max_length = 100)

class AnimalMedicationLog(models.Model):
    animal = models.ForeignKey(Animals, on_delete = models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

class Show(models.Model):
    animal = models.ForeignKey(Animals, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    ticket_price = models.DecimalField(max_digits = 5, decimal_places = 2)
    location = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)

class Products(models.Model):
    item_name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)