from rest_framework import serializers
from ...checkweather.models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city_name','country_name')