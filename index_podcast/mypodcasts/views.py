from allauth.socialaccount.models import SocialToken
from django.http import HttpResponse
from django.shortcuts import render
import requests

api_url = 'https://www.googleapis.com/youtube/v3/channels'


def test(request):
    t = SocialToken.objects.filter(account__user=request.user, account__provider='google')[0].token
    data = {
        'part': 'snippet',
        'mine': True,
        'access_token': t
        }
    #head = {"Authorization": "Bearer " + t}
    r = requests.get(api_url, params=data)
    return HttpResponse(r)