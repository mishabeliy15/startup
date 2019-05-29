from django.urls import path
from .views import test


app_name = 'mypodcasts'


urlpatterns = [
    path('', test, name='mylist'),
]
