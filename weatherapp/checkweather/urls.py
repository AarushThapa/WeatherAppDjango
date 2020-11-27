from django.urls import path
from .views import index, ListCity, AddCity, DeleteCity, UpdateCity, CityDetails

urlpatterns = [
    path('', index, name='home'),
    path('cities', ListCity.as_view(), name='allcity'),
    path('add-city', AddCity.as_view(), name='add_city'),
    path('update-city/<slug>', UpdateCity.as_view(), name='update_city'),
    path('delete-city/<slug>', DeleteCity.as_view(), name='delete_city'),
    path('city-detail/<slug>', CityDetails.as_view(), name='details'),

]
