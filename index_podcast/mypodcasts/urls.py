from django.urls import path
from .api_view import api_view_my_videos


app_name = 'mypodcasts'


urlpatterns = [
    path('api/videos', api_view_my_videos, name='my_videos'),
]
