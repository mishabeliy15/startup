import youtube_dl, threading
from index_podcast.settings import MEDIA_ROOT
from django.core.files import File
import os


def user_directory_path_audio(instance, filename):
    return 'user_{0}/podcast_{1}/audios/{2}'.format(instance.owner.id, instance.podcast.id, filename)


def iso_duration_to_seconds(s):
    s = s[2:]
    times = ['']
    k = 0
    mult = {'S': 1, 'M': 60, 'H': 3600}
    for i in s:
        if i.isdigit():
            times[k] += i
        else:
            times[k] = int(times[k]) * mult[i]
            times.append('')
            k += 1
    times.pop()
    return sum(times)


def download_mp3_from_video(url, name):
    outtmpl = MEDIA_ROOT + '/' + name + '.%(ext)s'
    ydl_opts = {
        'format': 'audio/m4a',
        'outtmpl': outtmpl,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_with_edit_model(video_id, obj):
    download_mp3_from_video("https://youtu.be/" + video_id, video_id)
    f = open(MEDIA_ROOT + '/' + video_id + '.m4a', 'rb')
    obj.audio_file.save(video_id + '.m4a', File(f))
    obj.processed = True
    obj.save()
    f.close()
    os.remove(MEDIA_ROOT + '/' + video_id + '.m4a')


def download_audio_thread(video_id, obj):
    t = threading.Thread(target=download_with_edit_model,
                         args=(video_id, obj))
    t.daemon = True
    t.start()