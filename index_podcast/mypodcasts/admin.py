from django.contrib import admin
from .models import Podcast, Episode


@admin.register(Podcast)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'created_date', 'image')


@admin.register(Episode)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'video_id', 'podcast', 'created_date', 'audio_file', 'image')

