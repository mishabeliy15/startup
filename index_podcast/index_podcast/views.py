from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index_podcast/index.html'


class PoliticsView(TemplateView):
    template_name = 'privacy_policy.html'
