from django.contrib import admin
from django.urls import include,path

from . import views

app_name = 'products'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
]