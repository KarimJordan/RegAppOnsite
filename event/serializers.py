from rest_framework import serializers
from .models import Event
from guest.models import Guest

class EventSerializer(serializers.ModelSerializer):

    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    no_of_guest = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'start_date',
            'end_date',
            'venue',
            'facebook_url',
            'instagram_url',
            'twitter_url',
            'no_of_guest'
        )

    @staticmethod
    def get_no_of_guest(obj):
        no_of_guest = Guest.objects.filter(event_id=obj.id).count()
        return no_of_guest