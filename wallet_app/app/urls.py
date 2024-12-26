from django.urls import path
from . import views


urlpatterns = [
    path('whole_data/', views.get_whole_data, name='whole_data'),
    path('wages/', views.get_wages_data, name='wages_data'),
    path('house_expenses/', views.get_house_expenses, name='house_expenses'),
    path('fuel_expenses/', views.get_fuel_expenses, name='fuel_expenses'),
    path('holidays_expenses/', views.get_holidays_expenses, name='holidays_expenses'),
    path('beverages_and_food/', views.get_beverages_and_food, name='beverages_and_food')
]
