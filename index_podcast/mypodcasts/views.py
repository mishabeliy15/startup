from allauth.socialaccount.models import SocialToken
from django.http import HttpResponse
from django.shortcuts import render
import requests

api_url = 'https://www.googleapis.com/youtube/v3/channels'
API_KEY = 'AIzaSyCHgG3JvxaTlD44zWsdUe8_F8_PS0qC5Aw'

def test(request):
    t = SocialToken.objects.filter(account__user=request.user, account__provider='google')[0].token
    data = {
        'part': 'snippet',
        'mine': True,
        'key': API_KEY
        }
    head = {"Authorization": "Bearer " + t}
    r = requests.get(api_url, params=data, headers=head)
    return HttpResponse(r)