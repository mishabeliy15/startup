from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PodcastCreateView(TemplateView, LoginRequiredMixin):
    template_name = 'mypodcasts/create.html'


class PodcastListView(TemplateView, LoginRequiredMixin):
    template_name = 'mypodcasts/mylist.html'