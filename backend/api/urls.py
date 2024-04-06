from django.urls import path

from . import views
#from .viws import api_home

urlpatterns = [
    path('', views.api_home, name="api_home"),
]