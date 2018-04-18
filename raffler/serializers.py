from rest_framework import serializers
from .models import Raffler, RafflerWinner, RafflerSelectionWinner
from event.models import Event
from guest.models import Guest


class RafflerSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = Raffler
        fields = (
            'event', 'id', 'title', 'num_of_draws', 'num_of_draws_done', 'label', 'prize_image', 'background_image',
            'draw_duration', 'item_duration', 'conditions')


class RafflerWinnerSerializer(serializers.ModelSerializer):
    raffle = serializers.PrimaryKeyRelatedField(queryset=Raffler.objects.all())
    guest = serializers.PrimaryKeyRelatedField(queryset=Guest.objects.all())

    class Meta:
        model = RafflerWinner
        fields = (
            'raffle', 'guest'
        )
