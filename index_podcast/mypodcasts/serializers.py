from .models import Podcast, Episode
from rest_framework import serializers


class EpisodeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False, required=False)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    audio_file = serializers.FileField(use_url=False, read_only=True)

    class Meta:
        model = Episode
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False, required=False)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    episodes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Podcast
        fields = '__all__'

    def get_episodes(self, instance):
        return EpisodeSerializer(instance.episodes.all().order_by('-created_date'), many=True).data
