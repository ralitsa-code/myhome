from . import views
from django.urls import path

urlpatterns = [
    path (
        '',
        views.brokers_list,
        name='brokers-list'
    ),
    path (
        '<int:broker_id>/',
        views.broker_details,
        name='broker-details'
    ),
    path (
        'create/',
        views.create_broker,
        name='create-broker'
    ),
    path (
        '<int:broker_id>/edit/',
        views.edit_broker,
        name='edit-broker'
    )
]