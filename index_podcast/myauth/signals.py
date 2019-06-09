from allauth.socialaccount.models import SocialToken
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
import requests


@receiver(user_logged_in)
def parse_channel_id(request, **kwargs):
    if request.user.channelid is None:
        t = SocialToken.objects.filter(account__user=request.user, account__provider='google')[0].token
        channel = get_about_channel(t)
        request.user.channelid = channel['items'][0]['id']
        request.user.save()


def get_about_channel(token):
    api_url = 'https://www.googleapis.com/youtube/v3/channels'
    data = {
        'part': 'snippet',
        'mine': 'true',
    }
    head = {"Authorization": "Bearer " + token}
    return requests.get(api_url, params=data, headers=head).json()