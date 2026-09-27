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
    ),
    path(
        'create/',
        views.create_property,
        name='create-property'
    ),
    path(
        '<int:property_id>/edit/',
        views.edit_property,
        name='edit-property'),
    path(
        '<int:property_id>/delete/',
        views.delete_property,
        name='delete-property'
    )
]