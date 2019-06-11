from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_view import api_view_my_videos, PodcastViewSet


app_name = 'mypodcasts'

router = DefaultRouter()
router.register(r'podcasts', PodcastViewSet)

urlpatterns = [
    path('api/videos', api_view_my_videos, name='my_videos'),
    path('api/', include(router.urls)),
]
