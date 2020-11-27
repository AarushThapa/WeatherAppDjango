from django.urls import path
from .views import loginView, logoutAction

urlpatterns = [
    path('login', loginView, name='login'),
    path('logout', logoutAction, name='logout')
]
