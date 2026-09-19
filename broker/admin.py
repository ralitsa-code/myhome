from django.contrib import admin
from broker.models import Broker


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
