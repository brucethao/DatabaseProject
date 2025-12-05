from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length = 100, unique = True, blank = False)
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

class Animal(models.Model):
    name = models.CharField(max_length = 100)
    species = models.CharField(max_length=100)
    age = models.IntegerField(default = 0)
    weight = models.DecimalField(max_digits = 5, decimal_places = 2)
    classification = models.ForeignKey(Classification, on_delete = models.CASCADE)
    animal_habitat = models.ForeignKey(Location, on_delete = models.CASCADE)


class Zookeeper(models.Model):
    wage = models.DecimalField(max_digits = 5, decimal_places = 2, default = 7.50)
    hours = models.DecimalField(max_digits = 5, decimal_places = 2, default = 8)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

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

    @receiver(post_save, sender=User)
    def sync_zookeeper_profile(sender, instance, created, **kwargs):
        if instance.is_zookeeper:
            # get_or_create prevents crashing if the profile already exists
            Zookeeper.objects.get_or_create(user=instance)
        else:
            # If they are NOT a zookeeper, find their profile and delete it
            Zookeeper.objects.filter(user=instance).delete()

    @receiver(post_delete, sender=Zookeeper)
    def remove_zookeeper_flag(sender, instance, **kwargs):
        # Updates the database with users that are not zookeepers ensuring the boolean field is false
        User.objects.filter(id=instance.user_id).update(is_zookeeper=False)