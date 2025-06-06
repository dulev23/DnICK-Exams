from django.contrib import admin
from .models import *
from datetime import datetime


# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName",)

    def has_add_permission(self, request):
        return request.user.is_superuser


class CharacteristicsAdmin(admin.ModelAdmin):
    list_display = ("name", "value",)

    def has_add_permission(self, request):
        return request.user.is_superuser


class AgentRealEstateInLine(admin.StackedInline):
    model = AgentRealEstate
    extra = 0


class CharacteristicsRealEstateInline(admin.StackedInline):
    model = CharacteristicRealEstate
    extra = 0


class RealEstateAdmin(admin.ModelAdmin):
    list_display = ("name", "location_description", "area")
    exclude = ("characteristic",)
    inlines = [AgentRealEstateInLine, CharacteristicsRealEstateInline]

    def has_add_permission(self, request):
        return Agent.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            AgentRealEstate.objects.create(real_estate=obj, agent=Agent.objects.filter(user=request.user).first())

    def has_change_permission(self, request, obj=None):
        return obj and AgentRealEstate.objects.filter(real_estate=obj, agent__user=request.user).exists()

    def has_delete_permission(self, request, obj=None):
        return not CharacteristicRealEstate.objects.filter(real_estate=obj).exists()


admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Characteristic, CharacteristicsAdmin)
