from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PodcastListView(TemplateView, LoginRequiredMixin):
    template_name = 'mypodcasts/my_podcasts.html'


class AddEpisodeView(TemplateView, LoginRequiredMixin):
    template_name = 'mypodcasts/add_episode.html'

