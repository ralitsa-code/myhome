from . import views
from django.urls import path

urlpatterns = [
    path(
        '',
        views.properties_list,
        name='properties-list'
    ),
    path(
        '<int:property_id>/',
        views.property_details,
        name='property-details'
    )
]