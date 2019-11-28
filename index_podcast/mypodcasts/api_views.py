from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions, viewsets
from .google_api import get_all_info_videos_of_channel
from .models import Podcast, Episode
from .serializers import PodcastSerializer, EpisodeSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser


@login_required
def api_view_my_videos(request):
    maxres = request.GET['maxRes'] if 'maxRes' in request.GET else 10
    videos = get_all_info_videos_of_channel(request.user.channelid, maxres)
    return JsonResponse(videos)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if 'user_id' in self.request.query_params:
            return Podcast.objects.filter(owner=self.request.query_params['user_id']).order_by("-created_date")
        elif 'all' in self.request.query_params and self.request.query_params['all']:
            return Podcast.objects.all().order_by("-created_date")
        else:
            return Podcast.objects.filter(owner=self.request.user).order_by("-created_date")


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    pagination_class = StandardResultsSetPagination
    parser_classes = (MultiPartParser, FormParser, JSONParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if 'user_id' in self.request.query_params:
            return Episode.objects.filter(owner=self.request.query_params['user_id']).order_by("-created_date")
        elif 'all' in self.request.query_params and self.request.query_params['all']:
            return Episode.objects.all().order_by("-created_date")
        else:
            return Episode.objects.filter(owner=self.request.user).order_by("-created_date")
