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
    )

]