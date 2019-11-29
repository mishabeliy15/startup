from rest_framework import serializers
from .models import ViewsPodcast, ViewsEpisode
from mypodcasts.models import Episode, Podcast
from mypodcasts.serializers import EpisodeSerializer, PodcastSerializer
from category.serializers import SubCategorySerializer


class ViewsEpisodeSerializer(serializers.ModelSerializer):
    episode_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ViewsEpisode
        fields = '__all__'

    def get_episode_info(self, obj):
        return EpisodeSerializer(obj.episode).data


class ViewsPodcastSerializer(serializers.ModelSerializer):
    podcast = PodcastSerializer(read_only=True)

    class Meta:
        model = ViewsPodcast
        fields = '__all__'


class ViewsPodcastSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewsPodcast
        fields = '__all__'


class EpisodeStatSerializer(serializers.ModelSerializer):
    stats = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Episode
        fields = '__all__'

    def get_stats(self, obj):
        views = ViewsEpisode.objects.filter(episode=obj)
        return ViewsEpisodeSerializer(views, many=True).data


class StatPodcastSerializer(serializers.ModelSerializer):
    categories = SubCategorySerializer(many=True, read_only=True)
    episodes = serializers.SerializerMethodField(read_only=True)
    stats = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Podcast
        fields = '__all__'

    def get_episodes(self, obj):
        return EpisodeStatSerializer(obj.episodes, many=True).data

    def get_stats(self, obj):
        views = ViewsPodcast.objects.filter(podcast=obj)
        return ViewsPodcastSimpleSerializer(views, many=True).data
