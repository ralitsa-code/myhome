from django.urls import path
from city import views


urlpatterns = [
    path(
        '',
        views.cities_list,
        name='cities-list'
    ),
    path(
        'create/',
        views.create_city,
        name='create-city'
    ),
    path(
        '<int:city_id>/edit/',
        views.edit_city,
        name='edit-city'
    ),
    path('<int:city_id>/delete/',
         views.delete_city,
         name='delete-city')
]