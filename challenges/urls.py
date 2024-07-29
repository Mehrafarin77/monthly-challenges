from django.urls import path
from .views import *

app_name = 'challenges'
urlpatterns = [
    path('months/', list_of_months, name='list_of_months'),
    path('<int:index>/', by_number, name='index'),
    path('<str:month>/', challenges, name='month'),
]
