from .models import Podcast
from rest_framework import serializers


class PodcastSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Podcast
        fields = '__all__'