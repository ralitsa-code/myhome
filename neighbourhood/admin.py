from django.contrib import admin
from neighbourhood.models import Neighbourhood


@admin.register(Neighbourhood)
class NeighbourhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name',)
    list_filter = ('name',)
