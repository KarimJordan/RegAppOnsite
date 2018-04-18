from django.db import models
from event.models import Event


class Guest(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    code = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_id.name + ':' + str(self.id)

    @staticmethod
    def update_guest(id, type):
        guest = Guest.objects.get(id=id)
        guest.type = type
        guest.save()

    @staticmethod
    def save_guest(event, code, type):
        guest = Guest(
            event_id=event,
            code=code,
            type=type
        )
        guest.save()
        return guest


class GuestInfoField(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=200)
    is_required = models.BooleanField(default=False)
    is_unique = models.BooleanField(default=False)
    is_email = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=True)
    is_hidden = models.BooleanField(default=False)
    order = models.IntegerField()

    def __str__(self):
        return self.event_id.name + ': ' + self.field_name

    @staticmethod
    def save_guest_info_field(event_id, field_name, is_required, is_unique, is_email, is_resolved, is_hidden, order):
        guest_info_field = GuestInfoField(
            event_id=event_id,
            field_name=field_name,
            is_required=is_required,
            is_unique=is_unique,
            is_email=is_email,
            is_resolved=is_resolved,
            order=order,
            is_hidden=is_hidden
        )
        guest_info_field.save()


class GuestInfo(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    guest_info_field_id = models.ForeignKey(GuestInfoField, on_delete=models.CASCADE, default=1)
    key = models.CharField(max_length=200, null=True, blank=True)
    value = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.key + ': ' + self.value + ': ' + self.event_id.name + ':' + str(self.guest_id.id)

    @staticmethod
    def save_guest_information(event_id, guest_id, guest_info_field, key, value):
        guest_info = GuestInfo(
            event_id=event_id,
            guest_id=guest_id,
            guest_info_field_id=guest_info_field,
            key=key,
            value=value
        )
        guest_info.save()

    @staticmethod
    def update_guest_information(guest_info_id, value):
        guest_info = GuestInfo.objects.get(id=guest_info_id)
        guest_info.value = value
        guest_info.save()

    @staticmethod
    def save_guest_bulk_create(data):
        bulk_guest_list = []
        for info in data:
            guest_info = GuestInfo(
                event_id=info['event_id'],
                guest_id=info['guest_id'],
                guest_info_field_id=info['guest_info_field_id'],
                key=info['key'],
                value=info['value'],
            )
            bulk_guest_list.append(guest_info)
        GuestInfo.objects.bulk_create(bulk_guest_list)
