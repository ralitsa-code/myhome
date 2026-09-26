from django.urls import path

from neighbourhood import views

urlpatterns = [
    path(
        '',
        views.neighbourhood_list,
        name='neighbourhood-list'
    ),
    path(
        'create/',
        views.create_neighbourhood,
        name='create-neighbourhood'
    ),
    path(
        '<int:neighbourhood_id>/edit/',
        views.edit_neighbourhood,
        name='edit-neighbourhood'
    ),
    path(
        '<int:neighbourhood_id>/delete/',
        views.delete_neighbourhood,
        name='delete-neighbourhood'
    )

]