from django.urls import path, include
from .views import PodcastDetailView, PodcastRSSView

app_name = 'publish_podcast'

urlpatterns = [
    path('podcasts/user_<int:user_id>/<int:pk>/', PodcastDetailView.as_view(), name="podcast-detail"),
    path('podcasts/user_<int:user_id>/<int:pk>/rss/', PodcastRSSView.as_view(), name="podcast-rss"),
]