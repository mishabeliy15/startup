from django.contrib import admin
from .models import ViewsPodcast, ViewsEpisode


@admin.register(ViewsPodcast)
class ViewsPodcastAdmin(admin.ModelAdmin):
    list_display = ('podcast', 'datetime')
    list_filter = ('podcast', 'datetime')

    class Meta:
        ordering = ['-datetime']


@admin.register(ViewsEpisode)
class ViewsPodcastAdmin(admin.ModelAdmin):
    list_display = ('episode', 'duration', 'datetime')
    list_filter = ('episode', 'duration', 'datetime')

    class Meta:
        ordering = ['-datetime', 'duration']
