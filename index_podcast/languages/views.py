from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Language
from django.urls import reverse_lazy


class LanguageListView(ListView):
    model = Language
    template_name = 'languages/list_language.html'


class LanguageCreateView(CreateView):
    model = Language
    fields = ('display', 'code')
    template_name = 'languages/add_language.html'
    success_url = reverse_lazy('languages:list')


class LanguageUpdateView(UpdateView):
    model = Language
    fields = ('display', 'code')
    template_name = 'languages/update_language.html'
    success_url = reverse_lazy('languages:list')


class LanguageDeleteView(DeleteView):
    model = Language
    fields = ('display', 'code')
    template_name = 'languages/update_language.html'
    success_url = reverse_lazy('languages:list')

