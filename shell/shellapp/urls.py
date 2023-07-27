
from django.urls import path

from shellapp.views import SelectCars

urlpatterns = [
    path('cars/', SelectCars.as_view(), name='show all cars'),

]
