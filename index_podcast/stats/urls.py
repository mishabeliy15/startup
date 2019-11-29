from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ViewsPodcastViewSet, ViewsEpisodeViewSet, StatsPodcastViewSet
from .views import StatsView

app_name = 'stats'

router = DefaultRouter()
router.register(r'podcast', ViewsPodcastViewSet, basename='views-podcast')
router.register(r'episode', ViewsEpisodeViewSet, basename='views-episode')
router.register(r'statistics', StatsPodcastViewSet, basename='statistics')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', StatsView.as_view(), name='stats'),
]
