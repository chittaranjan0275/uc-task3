from django.urls import path

from . import views

urlpatterns = [
    path('upcloud/users', views.index, name='index'),
]