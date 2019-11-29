from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import ViewsPodcast, ViewsEpisode
from .serializators import ViewsPodcastSerializer, ViewsEpisodeSerializer, StatPodcastSerializer
from django_filters.rest_framework import DjangoFilterBackend
from mypodcasts.models import Podcast


class ViewsPodcastViewSet(ModelViewSet):
    queryset = ViewsPodcast.objects.all().order_by('-datetime')
    serializer_class = ViewsPodcastSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('podcast', 'datetime',)


class ViewsEpisodeViewSet(ModelViewSet):
    queryset = ViewsEpisode.objects.all().order_by('-datetime')
    serializer_class = ViewsEpisodeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('episode', 'datetime', 'duration',)


class StatsPodcastViewSet(ReadOnlyModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = StatPodcastSerializer
