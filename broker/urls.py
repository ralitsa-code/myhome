from . import views
from django.urls import path

urlpatterns = [
    path (
        '',
        views.brokers_list,
        name='brokers-list'
    ),

]