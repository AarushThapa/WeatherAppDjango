from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..serializers.city import CitySerializer

from ...checkweather.models import City


class AddCityAPI(CreateAPIView):
    model = City
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            city = serializer.save()
            return Response({
                'args': True,
                'msg': "Success",
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
             return Response({
                'args': True,
                'msg': "failed",
                'data': serializer.erros
            }, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateCityAPI(RetrieveUpdateAPIView):
    queryset = City.objects.all()
    model = City
    serializer_class = CitySerializer
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response({
                'args': True,
                'msg': "Success",
                'data': serializer.data
            }, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), data=request.data)
        if serializer.is_valid():
            city = serializer.save()
            return Response({
                'args': True,
                'msg': "Success",
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
             return Response({
                'args': True,
                'msg': "failed",
                'data': serializer.erros
            }, status=status.HTTP_400_BAD_REQUEST)

