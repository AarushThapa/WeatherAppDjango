from django.urls import path
from ..viewsets.city import AddCityAPI, RetrieveUpdateCityAPI

city_urlpatterns = [
    path('add-city',AddCityAPI.as_view(),name='add_city_api'),
    path('cities/<int:pk>',RetrieveUpdateCityAPI.as_view(),name='update_city_api')

]