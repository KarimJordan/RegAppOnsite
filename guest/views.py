import logging

from rest_framework.authentication import BasicAuthentication
from django.shortcuts import render, redirect, reverse
from django.http import Http404
from rest_framework import status
from rest_framework import viewsets, renderers, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.contrib.auth.mixins import LoginRequiredMixin

from .serializers import GuestSerializer, GuestListSerializer, GuestInfoFieldSerializer, GuestListApiSerializer, \
    GuestInfoSerializer
from .models import Guest, GuestInfoField, GuestInfo

from event.models import Event

logger = logging.getLogger(__name__)


class GuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

    name = 'guest'

    event_id = ''

    # authentication_classes = (BasicAuthentication)

    def create(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_form.html'

        event_id = None
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = self.perform_create(serializer)
            for info in request.data['info_list']:
                guest_id = GuestInfoField.objects.get(event_id=info['event_id'], field_name=info['field_name'])
                event_id = Event.objects.get(id=info['event_id'])
                guest = GuestInfo.save_guest_information(
                    event_id=event_id,
                    guest_id=instance,
                    guest_info_field=guest_id,
                    key=info['key'],
                    value=info['value']
                )
            return redirect(reverse('event-detail', kwargs={'pk': event_id.id}))
        else:
            guest = serializer.data
            event_id = None
            if hasattr(self.request, 'session'):
                event_id = self.request.session.get('event_id', None)
            if event_id is None:
                return Http404()

            guest_fields = GuestInfoField.objects.filter(event_id=event_id).order_by('order').values('field_name',
                                                                                                     'order',
                                                                                                     'id',
                                                                                                     'event_id',
                                                                                                     'is_required',
                                                                                                     'is_unique',
                                                                                                     'is_email',
                                                                                                     'is_resolved')
            guest_fields = list(guest_fields)
            context = {
                'guest': guest,
                'guest_fields': guest_fields,
                'event_id': event_id,
            }
            response = Response(context)
            return response

    def perform_create(self, serializer):
        return serializer.save()

    @list_route(methods=['get'])
    def guest_list(self, request, *args, **kwargs):
        self.renderers_classes = [renderers.JSONRenderer()]
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def guest_add(self, request, *args, **kwargs):
        print(request.data)
        event_id = kwargs['pk']
        event = Event.objects.get(id=event_id)

        context = {}
        if 'id' in request.data and request.data['id'] != '':
            # update
            print('update')
            Guest.update_guest(request.data['id'], request.data['type'])

            for field in request.data['info_list']:
                GuestInfo.update_guest_information(
                    guest_info_id=field['id'],
                    value=field['value']
                )

                # GuestInfo.update_guest_information(
                #     guest_info_id=1,
                #     guest_id=request.data['id'],
                #     value=request.data['value'],
                # )
        else:
            # create
            code = request.data['code']
            type = request.data['type']

            instance = Guest.save_guest(
                event=event,
                type=type,
                code=code
            )

            guest_id = instance.id

            guest_info_data = request.data['info_list']

            for data in guest_info_data:
                field_name = data['key']
                guest_info_field_instance = GuestInfoField.objects.get(field_name=field_name, event_id__id=event.id)
                guest = GuestInfo.save_guest_information(
                    event_id=event,
                    guest_id=instance,
                    guest_info_field=guest_info_field_instance,
                    key=field_name,
                    value=data['value']
                )

        return Response(context)

    @detail_route(methods=['post'])
    def fields(self, request, *args, **kwargs):
        print(request.data)
        self.template_name = self.name + '/' + self.name + '_fields_form.html'
        event_id = kwargs['pk']
        serializer = self.get_serializer(data=request.data)
        response = Response('fields')
        if 'guest_info_fields' in request.data:
            guest_info_fields = request.data['guest_info_fields']
            for field in guest_info_fields:
                if 'id' in field:
                    field_name = field['field_name']
                    order = field['order']
                    is_required = field['is_required']
                    is_unique = field['is_unique']
                    is_email = field['is_email']
                    is_resolved = field['is_resolved']
                    event_id = event_id
                    id = GuestInfoField.objects.get(id=field['id'])
                    data = {
                        'field_name': field_name,
                        'order': order,
                        'is_required': is_required,
                        'is_unique': is_unique,
                        'is_email': is_email,
                        'is_resolved': is_resolved,
                        'event_id': event_id
                    }
                    serializer = self.get_serializer(id, data=data)
                    if serializer.is_valid():
                        serializer.save()
                        response = redirect(reverse('event-detail', kwargs={'pk': event_id}))
        elif 'delete' in request.data:
            id = request.data['id']
            instance = GuestInfoField.objects.get(id=id)
            self.perform_destroy(instance)
            response = redirect(reverse('event-detail', kwargs={'pk': event_id}))
        elif 'update_hidden' in request.data:
            if 'id' in request.data:
                id = request.data['id']
                instance = GuestInfoField.objects.get(id=id)
                data = {
                    'field_name': request.data['field_name'],
                    'event_id': request.data['event_id'],
                    'order': request.data['order'],
                    'is_hidden': request.data['hidden']
                }
                serializer = self.get_serializer(instance, data=data)
                serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = redirect(reverse('event-detail', kwargs={'pk': event_id}))
        elif serializer.is_valid():
            self.perform_create(serializer)
            response = redirect(reverse('event-detail', kwargs={'pk': event_id}))
        else:
            guest_i_fields = serializer.data
            guest_info_fields = GuestInfoField.objects.filter(event_id=event_id).order_by('order').values('field_name',
                                                                                                          'order',
                                                                                                          'id',
                                                                                                          'is_hidden',
                                                                                                          'is_required',
                                                                                                          'is_unique',
                                                                                                          'is_email',
                                                                                                          'is_resolved')
            guest_info_fields = list(guest_info_fields)
            context = {
                'guest_i_fields': guest_i_fields,
                'guest_info_fields': guest_info_fields,
                'event_id': event_id
            }
            response = Response(context)
        return response

    @detail_route(methods=['post'])
    def udpate_order(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_302_FOUND)
        if 'id' in request.data:
            event_id = request.data['event_id']
            id = request.data['id']
            order = request.data['order']
            is_required = request.data['is_required']
            is_unique = request.data['is_unique']
            is_email = request.data['is_email']
            is_resolved = request.data['is_resolved']
            is_hidden = request.data['is_hidden']

            guest_info_field = GuestInfoField.objects.filter(id=id)
            guest_info_field.update(
                order=order,
                is_required=is_required,
                is_unique=is_unique,
                is_email=is_email,
                is_resolved=is_resolved,
                is_hidden=is_hidden
            )
        # response = redirect(reverse('event-detail', args={'pk': event_id}))
        return response

    @detail_route(methods=['post'])
    def delete_info(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        if 'guest_id' in request.data:
            guest_id = request.data['guest_id']
            instance = Guest.objects.get(id=guest_id)
            instance.delete()
        return response

    @detail_route(methods=['post'])
    def update_info(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_302_FOUND)
        if 'id' in request.data:
            id = request.data['id']
            value = request.data['value']
            key = request.data['key']
            event_id = request.data['event_id']
            guest_id = request.data['guest_id']
            guest_info_field_id = request.data['guest_info_field_id']
            guest_info = GuestInfo.objects.get(id=id)
            data = {
                'value': value,
                'key': key,
                'event_id': event_id,
                'guest_id': guest_id,
                'guest_info_field_id': guest_info_field_id
            }
            serializer = self.get_serializer(guest_info, data=data)
            if serializer.is_valid():
                serializer.save()
                response = redirect(reverse('event-detail', kwargs={'pk': event_id}))

        return response

    def post(self, request, *args, **kwargs):
        if request.resolver_match.url_name == self.name + '-detail':
            if '_method' in request.data and request.data['_method'] == 'delete':
                response = self.destroy(request, *args, **kwargs)
            else:
                self.action = 'update'
                response = super(GuestViewSet, self).update(request, *args, *kwargs)
        elif self.action == 'delete_info':
            response = super(GuestViewSet, self).delete_info(request, *args, **kwargs)
        elif self.request.resolver_match.url_name == 'guest_add':
            response = super(GuestViewSet, self).guest_add(request, *args, **kwargs)
        elif self.action == 'update_info':
            response = super(GuestViewSet, self).update_info(request, *args, **kwargs)
        elif self.action == 'udpate_order':
            response = super(GuestViewSet, self).udpate_order(request, *args, **kwargs)
        elif self.action == 'fields':
            response = super(GuestViewSet, self).fields(request, *args, **kwargs)
        else:
            response = super(GuestViewSet, self).post(request, *args, **kwargs)
        return response

    def get_serializer(self, *args, **kwargs):
        serializer = super(GuestViewSet, self).get_serializer(*args, **kwargs)
        return serializer

    def get_serializer_class(self):
        print(self.request.resolver_match.url_name)
        if self.action == 'list':
            return GuestListSerializer
        elif self.action == 'guest_list':
            return GuestListApiSerializer
        elif self.action == 'update_info':
            return GuestInfoSerializer
        elif self.action == 'fields':
            return GuestInfoFieldSerializer
        return self.serializer_class

    def get_queryset(self):
        queryset = super(GuestViewSet, self).get_queryset()
        if self.action == 'fields':
            event_id = None
            if hasattr(self.request, 'session'):
                event_id = self.request.session.get('event_id', None)
            if event_id is None:
                return Http404()
            queryset = GuestInfoField.objects.filter(event_id=event_id).all()
        elif self.action == 'guest_list':
            event_id = self.kwargs['pk']
            queryset = Guest.objects.filter(event_id=event_id).all()
        return queryset

    def get_renderers(self):
        print(self.request.resolver_match.url_name)
        if self.request.resolver_match.url_name == 'guest_list':
            renderers_classes = [renderers.JSONRenderer()]
        elif self.action == 'delete_info':
            renderers_classes = [renderers.JSONRenderer()]
        elif self.action == 'udpate_order':
            renderers_classes = [renderers.JSONRenderer()]
        elif self.request.resolver_match.url_name == 'guest-guest-add':
            renderers_classes = [renderers.JSONRenderer()]
        else:
            renderers_classes = [renderers.TemplateHTMLRenderer()]
        return renderers_classes

    def dispatch(self, request, *args, **kwargs):
        return super(GuestViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        serializer = super(GuestViewSet, self).get_serializer(*args, **kwargs)
        return serializer
