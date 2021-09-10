from rest_framework import serializers

from WineOpener.models import Topic

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields  = ["comment"]