from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions, viewsets
from .google_api import get_all_info_videos_of_channel
from .models import Podcast
from .serializers import PodcastSerializer
from .permissions import IsOwnerOrReadOnly


@login_required
def api_view_my_videos(request):
    maxres = request.GET['maxRes'] if 'maxRes' in request.GET else 10
    videos = get_all_info_videos_of_channel(request.user.channelid, maxres)
    return JsonResponse(videos)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Podcast.objects.filter(owner=self.request.user).order_by("-created_date")