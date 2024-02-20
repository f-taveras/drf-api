from django.contrib import admin
from .models import Planet


class PlanetAdmin(admin.ModelAdmin):
    readonly_fields = ("highlighted",)

admin.site.register(Planet, PlanetAdmin)