from django.views.generic import DetailView
from mypodcasts.models import Podcast, Episode


class PodcastDetailView(DetailView):
    model = Podcast
    template_name = 'publish_podcasts/podcast-1.html'

    def get_queryset(self):
        return Podcast.objects.filter(owner=self.kwargs['user_id'])


class PodcastRSSView(DetailView):
    model = Podcast
    template_name = 'publish_podcasts/feed.rss'

    def get_queryset(self):
        return Podcast.objects.filter(owner=self.kwargs['user_id'])
