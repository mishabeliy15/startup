from django.db import models
from .services import download_audio_thread, user_directory_path_audio
from category.models import SubCategory


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/podcasts/img/{2}'.format(instance.owner.id, instance.id, filename)


class Podcast(models.Model):
    owner = models.ForeignKey('myauth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=128, blank=True)
    explicit = models.BooleanField(default=False)
    language = models.CharField(max_length=6, default="en")
    category = models.CharField(max_length=128, blank=True)
    link_spotify = models.URLField(blank=True)
    link_google = models.URLField(blank=True)
    link_apple = models.URLField(blank=True)
    categories = models.ManyToManyField(SubCategory, blank=True)

    def __str__(self):
        return self.title


class Episode(models.Model):
    owner = models.ForeignKey('myauth.User', on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    video_id = models.CharField(max_length=64, unique=True)
    audio_file = models.FileField(upload_to=user_directory_path_audio, blank=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    description = models.TextField(blank=True)
    duration = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            download_audio_thread(self.video_id, self)
        return super().save(*args, **kwargs)

