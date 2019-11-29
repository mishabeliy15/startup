from django.views.generic import TemplateView
from mypodcasts.models import Podcast


class IndexView(TemplateView):
    template_name = 'index_podcast/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = Podcast.objects.all().order_by("-created_date")
        context['last_podcasts'] = objects[:10]
        last_index = []
        count = 0
        for i in objects:
            if i.link_spotify or i.link_google or i.link_apple:
                last_index.append(i)
                count += 1
            if count >= 10:
                break
        context['last_indexes'] = last_index
        return context


class PoliticsView(TemplateView):
    template_name = 'privacy_policy.html'


class IntroPage(TemplateView):
    template_name = 'landings/intro_landing.html'


class SettingsView(TemplateView):
    template_name = 'category/base.html'
