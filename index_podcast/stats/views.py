from django.shortcuts import render
from django.views.generic import TemplateView


class StatsView(TemplateView):
    template_name = 'stats/stats.html'
