import requests

API_KEY = 'AIzaSyAu4Hl8gxM7-qVxt25tsj6rHkrj5K1rR_4'


def get_all_video_of_channel(channelid, maxres=10):
    api_url = 'https://www.googleapis.com/youtube/v3/search'
    data = {
        'part': 'snippet',
        'channelId': channelid,
        'type': 'video',
        'key': API_KEY,
        'maxResults': maxres
    }
    return requests.get(api_url, params=data).json()


def get_more_info_videos(video_ids, part=('statistics', 'contentDetails')):
    api_url = 'https://www.googleapis.com/youtube/v3/videos'
    data = {
        'key': API_KEY,
        'part': ','.join(part),
        'id': ','.join(video_ids)
    }
    return requests.get(api_url, params=data).json()


def get_all_info_videos_of_channel(channelid, maxRes=10, **kwargs):
    videos = get_all_video_of_channel(channelid, maxRes)
    ids = [i['id']['videoId'] for i in videos['items']]
    info = get_more_info_videos(ids)
    for i in range(len(videos['items'])):
        videos['items'][i]['statistics'] = info['items'][i]['statistics']
        videos['items'][i]['contentDetails'] = info['items'][i]['contentDetails']
    return videos
