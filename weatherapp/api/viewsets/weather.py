import http.client

from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.weather import WeatherSerializer

class ViewWeatherAPI(APIView):

    serializer_class = WeatherSerializer

    # def get(self, *args, **kwargs):
    #     data = [{'city': "city name"}]
    #     serailizer = self.get_serializer(data)
    #     return Response({
    #         'ack': True,
    #         'data': serailizer.data
    #     }, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serailizer = WeatherSerializer(data=request.data)

        if serailizer.is_valid():
            validated_data = serailizer.validated_data
            city = validated_data.get('city')
            print(city)
            conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")
            headers = {
                'x-rapidapi-key': "7d2f8a310fmsh6237cd22123bc70p1ee6d9jsn4545eb758793",
                'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
                }
            conn.request("GET", f"/find?q={city}&cnt=1&mode=null&lon=0&type=link%2C%20accurate&lat=0&units=imperial%2C%20metric", headers=headers)

            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
          
            return Response({
                "ack": True,
                'data': data
            },status=status.HTTP_200_OK)
        else: 
             return Response({
                "ack": True,
                "msg": "Failed",
                "data": serailizer.errors
            }, status=status.HTTP_400_BAD_REQUEST)  
