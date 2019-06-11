from .models import Podcast
from rest_framework import serializers


class PodcastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast
        fields = '__all__'