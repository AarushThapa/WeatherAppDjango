from .weather import weather_urlpatterns 
from .city import city_urlpatterns

urlpatterns = weather_urlpatterns
urlpatterns += city_urlpatterns 