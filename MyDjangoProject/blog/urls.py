from django.urls import path
from .views import home, homes, add_post

urlpatterns = [
    path('',home, name = 'home'),
    path('homes/', homes, name='homes'),
    path('add_post/', add_post, name='add_post'),

]

