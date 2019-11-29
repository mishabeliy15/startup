from rest_framework.viewsets import ModelViewSet
from .models import ViewsPodcast, ViewsEpisode
from .serializators import ViewsPodcastSerializer, ViewsEpisodeSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ViewsPodcastViewSet(ModelViewSet):
    queryset = ViewsPodcast.objects.all().order_by('-datetime')
    serializer_class = ViewsPodcastSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('podcast', 'datetime',)


class ViewsEpisodeViewSet(ModelViewSet):
    model = ViewsEpisode.objects.all().order_by('-datetime')
    serializer_class = ViewsEpisodeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('episode', 'datetime', 'duration',)
