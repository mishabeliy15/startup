from rest_framework import serializers
from .models import ViewsPodcast, ViewsEpisode


class ViewsPodcastSerializer(serializers.ModelSerializer):

    class Meta:
        model = ViewsPodcast
        fields = '__all__'


class ViewsEpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ViewsEpisode
        fields = '__all__'
