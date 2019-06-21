from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new, name='plate_new'),
    path('overview', views.overview)
]