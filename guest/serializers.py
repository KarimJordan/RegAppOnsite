from rest_framework import serializers
from .models import Guest, GuestInfo, GuestInfoField

from event.models import Event

import logging

logger = logging.getLogger(__name__)


class GuestListSerializer(serializers.ModelSerializer):
    event_id = serializers.StringRelatedField(source='event.id', read_only=True)

    class Meta:
        model = Guest
        fields = ('event_id', 'code', 'type')

    @staticmethod
    def get_info_list(obj):
        info_list = ''
        return info_list


class GuestInfoFieldSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = GuestInfoField
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = Guest
        fields = ('event_id', 'type', 'code')


class GuestInfoSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    guest_id = serializers.PrimaryKeyRelatedField(queryset=Guest.objects.all())
    guest_info_field_id = serializers.PrimaryKeyRelatedField(queryset=GuestInfoField.objects.all())
    is_required = serializers.StringRelatedField(source='guest_info_field_id.is_required')
    is_unique = serializers.StringRelatedField(source='guest_info_field.is_unique')
    is_email = serializers.StringRelatedField(source='guest_info_field.is_email')
    is_resolved = serializers.StringRelatedField(source='guest_info_field.is_resolved')
    is_hidden = serializers.StringRelatedField(source='guest_info_field.is_hidden')

    class Meta:
        model = GuestInfo
        fields = ('event_id', 'guest_id', 'guest_info_field_id', 'is_required', 'is_unique', 'is_email', 'is_resolved',
                  'is_hidden', 'key', 'value')


class GuestListApiSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    info_list = serializers.SerializerMethodField()

    class Meta:
        model = Guest
        fields = ('event_id', 'id', 'code', 'type', 'info_list')

    @staticmethod
    def get_info_list(obj):
        info_list = []
        guest_info = GuestInfo.objects.filter(event_id=obj.event_id, guest_id=obj.id).all()
        for info in guest_info:
            information = {
                'id': info.id,
                'event_id': info.event_id.id,
                'guest_id': info.guest_id.id,
                'key': info.key,
                'value': info.value,
                'is_required_field': info.guest_info_field_id.is_required,
                'is_unique': info.guest_info_field_id.is_unique,
                'is_email': info.guest_info_field_id.is_email,
                'is_resolved': info.guest_info_field_id.is_resolved,
                'is_hidden': info.guest_info_field_id.is_hidden,
            }
            info_list.append(information)
        return info_list
