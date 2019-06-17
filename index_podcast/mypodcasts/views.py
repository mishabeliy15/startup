from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PodcastListView(LoginRequiredMixin, TemplateView):
    template_name = 'mypodcasts/my_podcasts.html'


class AddEpisodeView(LoginRequiredMixin, TemplateView):
    template_name = 'mypodcasts/add_episode.html'

