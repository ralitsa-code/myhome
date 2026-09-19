from django.contrib import admin
from property.models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'neighborhood', 'area', 'price')
    search_fields = ('property_type', 'neighborhood__name', 'neighborhood__city__name')
    list_filter = ('property_type', 'neighborhood__name', 'neighborhood__city__name')