from django.urls import path
from .views import PodcastHTMLView, EpisodesView, EpisodesPDF, PodcastsPdf

app_name = 'reports'

urlpatterns = [
    path('podcasts/html', PodcastHTMLView.as_view(), name='podcasts-html'),
    path('episodes/html', EpisodesView.as_view(), name='episodes-html'),
    path('podcasts/pdf', PodcastsPdf.as_view(), name='podcasts-pdf'),
    path('episodes/pdf', EpisodesPDF.as_view(), name='episodes-pdf'),
]
