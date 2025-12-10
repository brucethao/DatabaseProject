from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Zootopia.models import Animal, User, Location, Classification, Zookeeper, FunFact, AnimalMedicationLog, AnimalFeedingLog, Food, Diet, Medication

# Register your models here.

# Adjusting admin sites to show useful information to the admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_zookeeper')

     # This adds your custom 'is_zookeeper' field to the "Edit User" page
    fieldsets = UserAdmin.fieldsets + (
        ('Zootopia Info', {'fields': ('is_zookeeper',)}),
    )
    # This adds your custom 'is_zookeeper' field to the "Add User" page
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Zootopia Info', {'fields': ('is_zookeeper',)}),
    )

class CustomAnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'weight', 'get_continent')

    def get_continent(self, obj):
        return obj.animal_habitat.continent
    get_continent.short_description = 'Continent'

class CustomLocationAdmin(admin.ModelAdmin):
    list_display = ('continent', 'habitat')

class CustomClassificationAdmin(admin.ModelAdmin):
    list_display = ('type',)

class CustomZookeeperAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'get_fullname')

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_fullname(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name
    get_fullname.short_description = 'Fullname'

class CustomFoodAdmin(admin.ModelAdmin):
    list_display = ('food_name',)

class CustomDietAdmin(admin.ModelAdmin):
    list_display = ('get_animal_name', 'get_food_name')

    def get_food_name(self, obj):
        return obj.food_name.food_name
    get_food_name.short_description = 'Food'

    def get_animal_name(self, obj):
        return obj.animal.name
    get_animal_name.short_description = 'Animal'

class CustomMedicationAdmin(admin.ModelAdmin):
    list_display = ('get_medication_name',)

    def get_medication_name(self, obj):
        return obj.medication_name
    get_medication_name.short_description = 'Medication'

class CustomMedicationLogAdmin(admin.ModelAdmin):
    list_display = ('get_animal_name', 'get_medication_name', 'get_amount', 'get_date')

    def get_animal_name(self, obj):
        return obj.animal.name
    get_animal_name.short_description = 'Animal'

    def get_medication_name(self, obj):
        return obj.medication.medication_name
    get_medication_name.short_description = 'Medication'

    def get_amount(self, obj):
        return obj.medication_amount
    get_amount.short_description = 'Amount'

    def get_date(self, obj):
        return obj.date
    get_date.short_description = 'Date'

class CustomFunFactAdmin(admin.ModelAdmin):
    list_display = ('get_animal_name',)

    def get_animal_name(self, obj):
        return obj.animal.name
    get_animal_name.short_description = 'Animal'

class CustomAnimalFeedingLogAdmin(admin.ModelAdmin):
    list_display = ('get_animal_name', 'get_food_name', 'get_amount', 'get_lastfed', 'get_zookeeper')

    def get_animal_name(self, obj):
        return obj.animal.name
    get_animal_name.short_description = 'Animal'

    def get_food_name(self, obj):
        return obj.food_name.food_name
    get_food_name.short_description = 'Food'

    def get_amount(self, obj):
        return obj.amount
    get_amount.short_description = 'Amount'

    def get_lastfed(self, obj):
        return obj.last_fed
    get_lastfed.short_description = 'Last Fed'

    def get_zookeeper(self, obj):
        return obj.zookeeper.user.first_name
    get_zookeeper.short_description = 'Zookeeper'


admin.site.register(User, CustomUserAdmin)
admin.site.register(Animal, CustomAnimalAdmin)
admin.site.register(Location, CustomLocationAdmin)
admin.site.register(Classification, CustomClassificationAdmin)
admin.site.register(Zookeeper, CustomZookeeperAdmin)
admin.site.register(Food, CustomFoodAdmin)
admin.site.register(Diet, CustomDietAdmin)
admin.site.register(Medication, CustomMedicationAdmin)
admin.site.register(FunFact, CustomFunFactAdmin)
admin.site.register(AnimalMedicationLog, CustomMedicationLogAdmin)
admin.site.register(AnimalFeedingLog, CustomAnimalFeedingLogAdmin)

