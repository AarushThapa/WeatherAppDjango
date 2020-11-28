import http.client
import json

from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.shortcuts import render

from .forms import Cityform, Searchform
from .models import City
from ..permission import LoginMixin

def index(request):
    if request.method == "GET":
        form = Searchform
        context = {
            'form' : form
        }
        return render(request, 'weather/index.html', context)    
    else:
        form = Searchform

        city = request.POST['search_field']
        conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")
        headers = {
            'x-rapidapi-key': "7d2f8a310fmsh6237cd22123bc70p1ee6d9jsn4545eb758793",
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }
        conn.request("GET", f"/find?q={city}&cnt=1&mode=null&lon=0&type=link%2C%20accurate&lat=0&units=metric", headers=headers)

        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        data = json.loads(data)

        list = data['list']
        list = list[0]

        city = list['name']

        weather = list['weather'][0]['main']

        temp = list['main']['temp']
        context = {
            'data' : data,
            'city': city,
            'weather':weather,
            'temp': temp,
            'form' : form
        }
        return render(request, 'weather/index.html', context)


class AddCity(LoginMixin, CreateView):
    model = City
    form_class = Cityform
    template_name = 'city/add_city.html'
    success_url = reverse_lazy('allcity')

    def form_valid(self,form):
        if form.is_valid():
            form.save() 
            return super().form_valid(form)
        else:
            return HttpResponse("Invalid")



class DeleteCity(LoginMixin, DeleteView):
    model = City
    template_name = 'city/delete_city.html'
    context_object_name = 'city'
    success_url = reverse_lazy('allcity')

    def get_object(self, **kwargs):
        city = get_object_or_404(City, slug=self.kwargs.get('slug'))
        return city
    

class UpdateCity(LoginMixin, UpdateView):
    model = City
    form_class = Cityform
    template_name = 'city/update_city.html'
    context_object_name = 'city'
    success_url = reverse_lazy('allcity')

    def get_object(self, **kwargs):
        city = get_object_or_404(City, slug=self.kwargs.get('slug'))
        return city

    def form_valid(self, form):
        return super().form_valid(form)


class CityDetails(LoginMixin, DetailView):
    model = City
    template_name = 'city/city_detail.html'
    context_object_name = 'city'

    def get_object(self, **kwargs):
        city = get_object_or_404(City, slug=self.kwargs.get('slug'))
        return city


class ListCity(ListView):
    model = City
    template_name = 'city/all_city.html'
    context_object_name = 'cities'

