from django.db import models


class ViewsPodcast(models.Model):
    podcast = models.ForeignKey('mypodcasts.Podcast', related_name="views", on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.datetime}] {self.podcast.title}"


class ViewsEpisode(models.Model):
    episode = models.ForeignKey('mypodcasts.Episode', related_name="views", on_delete=models.CASCADE)
    duration = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.datetime} | {self.episode.title}] Seconds: {self.duration}"
