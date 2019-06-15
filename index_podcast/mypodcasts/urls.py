from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_view import api_view_my_videos, PodcastViewSet, EpisodeViewSet
from .views import PodcastCreateView, PodcastListView

app_name = 'mypodcasts'

router = DefaultRouter()
router.register(r'podcasts', PodcastViewSet)
router.register(r'episodes', EpisodeViewSet)

urlpatterns = [
    path('api/videos', api_view_my_videos, name='my_videos'),
    path('api/', include(router.urls)),
    path('create/', PodcastCreateView.as_view(), name='create'),
    path('', PodcastListView.as_view(), name="list"),
]
