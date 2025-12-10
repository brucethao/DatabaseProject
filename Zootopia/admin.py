from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Zootopia.models import Animal, User, Location, Classification, Zookeeper, FunFact, AnimalMedicationLog, AnimalFeedingLog, Food, Diet, Medication

# Register your models here.

# Adjusting hashing with our custom user model
class CustomUserAdmin(UserAdmin):
    # This ensures that when you view a list of users, you see these columns
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_zookeeper')
     # This adds your custom 'is_zookeeper' field to the "Edit User" page
    fieldsets = UserAdmin.fieldsets + (
        ('Zootopia Info', {'fields': ('is_zookeeper',)}),
    )
    # This adds your custom 'is_zookeeper' field to the "Add User" page
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Zootopia Info', {'fields': ('is_zookeeper',)}),
    )
admin.site.register(User, CustomUserAdmin)
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

