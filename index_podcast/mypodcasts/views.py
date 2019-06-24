from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Podcast


class PodcastListView(LoginRequiredMixin, TemplateView):
    template_name = 'mypodcasts/my_podcasts.html'


class AddEpisodeView(LoginRequiredMixin, TemplateView):
    template_name = 'mypodcasts/add_episode.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'podcast' in self.request.GET:
            context['podcast'] = self.request.GET['podcast']
        return context


class EditPodcastView(LoginRequiredMixin, DetailView):
    template_name = 'mypodcasts/edit.html'
    model = Podcast

    def get_queryset(self):
        return Podcast.objects.filter(owner=self.request.user)