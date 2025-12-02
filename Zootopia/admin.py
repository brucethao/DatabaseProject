from django.contrib import admin

from Zootopia.models import Animal, User, Location, Classification, Zookeeper, FunFact, AnimalMedicationLog, AnimalFeedingLog, Food, Diet, Medication

# Register your models here.
admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Location)
admin.site.register(Classification)
admin.site.register(Zookeeper)
admin.site.register(Food)
admin.site.register(Diet)
admin.site.register(Medication)
admin.site.register(FunFact)
admin.site.register(AnimalMedicationLog)
admin.site.register(AnimalFeedingLog)