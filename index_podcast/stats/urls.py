from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ViewsPodcastViewSet, ViewsEpisodeViewSet

app_name = 'stats'

router = DefaultRouter()
router.register(r'podcast', ViewsPodcastViewSet, basename='views-podcast')
router.register(r'episode', ViewsEpisodeViewSet, basename='views-episode')


urlpatterns = [
    path('api/', include(router.urls)),
]
