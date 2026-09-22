
from django.urls import path

from feature import views



urlpatterns = [
    path(
        '',
        views.feature_list,
        name='features-list'
    ),

    path(
        'create/',
        views.create_feature,
        name='create-feature'
    ),
    path(
        '<int:feature_id>/edit/',
        views.edit_feature,
        name='edit-feature'
    ),

    path('<int:feature_id>/delete/',
         views.delete_feature,
         name='delete-feature')



]