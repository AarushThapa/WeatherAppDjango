from django.urls import path
from ..viewsets.weather import ViewWeatherAPI

weather_urlpatterns = [
    path('view-weather',ViewWeatherAPI.as_view(),name='view_weather')
]