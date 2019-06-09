from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .google_api import get_all_info_videos_of_channel


@login_required
def api_view_my_videos(request):
    maxres = request.GET['maxRes'] if 'maxRes' in request.GET else 10
    videos = get_all_info_videos_of_channel(request.user.channelid, maxres)
    return JsonResponse(videos)