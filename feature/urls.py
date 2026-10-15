
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
        views.CreateFeature.as_view(),
        name='create-feature'
    ),
    path(
        '<int:pk>/edit/',
        views.EditFeatureView.as_view(),
        name='edit-feature'
    ),

    path('<int:feature_id>/delete/',
         views.delete_feature,
         name='delete-feature')



]