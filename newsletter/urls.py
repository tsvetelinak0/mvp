from django.urls import path
from .views import (home, contact)


urlpatterns = [
    # Examples:
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
   
] 

