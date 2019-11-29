from django.contrib import admin
from .models import ViewsPodcast


@admin.register(ViewsPodcast)
class ViewsPodcastAdmin(admin.ModelAdmin):
    list_display = ('podcast', 'datetime')
    list_filter = ('podcast', 'datetime')

    class Meta:
        ordering = ['-datetime']
