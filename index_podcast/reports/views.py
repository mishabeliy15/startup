from django.views.generic import ListView
from mypodcasts.models import Podcast, Episode
from easy_pdf.views import PDFTemplateResponseMixin


class PodcastHTMLView(ListView):
    model = Podcast
    template_name = 'reports/podcasts.html'


class EpisodesView(ListView):
    model = Podcast
    template_name = 'reports/episodes.html'


class PodcastsPdf(PDFTemplateResponseMixin, ListView):
    model = Podcast
    template_name = 'reports/podcasts.html'


class EpisodesPDF(PDFTemplateResponseMixin, ListView):
    model = Podcast
    template_name = 'reports/episodes.html'
