from django.views.generic import DetailView
from mypodcasts.models import Podcast, Episode
from stats.models import ViewsPodcast


class PodcastDetailView(DetailView):
    model = Podcast
    template_name = 'publish_podcasts/podcast-1.html'

    def get_queryset(self):
        return Podcast.objects.filter(owner=self.kwargs['user_id'])

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        ViewsPodcast(podcast=obj).save()
        return obj


class PodcastRSSView(DetailView):
    model = Podcast
    template_name = 'publish_podcasts/feed.rss'

    def get_queryset(self):
        return Podcast.objects.filter(owner=self.kwargs['user_id'])
