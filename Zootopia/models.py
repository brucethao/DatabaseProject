from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.

# AbstractUser allows our user class to inherit Django's user fields (Username, password, first name, last name, etc.)
# while using its authentication system in addition to our own fields
class User(AbstractUser):
    is_zookeeper = models.BooleanField(default = False)
#Ensures that zookeeper object is created when a user is created to be a zookeeper
    #Also deletes zookeeper object when user is removed as a zookeeper

class Zookeeper(models.Model):
    wage = models.DecimalField(max_digits = 5, decimal_places = 2, default = 7.50)
    hours = models.DecimalField(max_digits = 5, decimal_places = 2, default = 8)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

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

class Location(models.Model):
    continent = models.CharField(max_length = 100)
    habitat = models.CharField(max_length = 100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['continent', 'habitat'],
                name='unique_continent_habitat',
            )
        ]
# FIXED!
#unique shouldn't be the key if there is an idea also having uniqueness
#prevents proper data to be stored (Ex. Continent: "North America" Habitat: "Wetlands")
# & Continent: "North America" Habitat: "Wetlands") can't be stored together)

class Classification(models.Model):
    type = models.CharField(max_length = 100)

class Animal(models.Model):
    name = models.CharField(max_length = 100, default="")
    species = models.CharField(max_length=100)
    age = models.IntegerField(default = 0)
    weight = models.DecimalField(max_digits = 15, decimal_places = 2)
    classification = models.ForeignKey(Classification, on_delete = models.CASCADE)
    animal_habitat = models.ForeignKey(Location, on_delete = models.CASCADE)
#Cannot add more than 3 digits before decimal point. - FIXED!

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
    medication_name = models.CharField(max_length = 100)
    # removed animal, it is already in animal-medication log
    # moved amount to med-logs

class FunFact(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    bio = models.CharField(max_length = 1024)
    fun_facts = models.CharField(max_length = 1024)
    #Varchar length should be increased for descriptions. - FIXED!

class AnimalMedicationLog(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete = models.CASCADE)
    medication_amount = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    date = models.DateTimeField(auto_now_add = True)

class Show(models.Model):
    name = models.CharField(max_length = 100, default="") # name instead of animals, we can state the animals in description
    date = models.DateTimeField(auto_now_add = True)
    ticket_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    location = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1024)

class Product(models.Model):
    item_name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)