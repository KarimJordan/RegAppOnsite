import logging
import io
import xlsxwriter
import collections
import json
import datetime
from django.http import Http404
from django.contrib.auth.decorators import login_required
from pyexcel_xlsx import get_data, save_data
from collections import defaultdict, Counter
from django.http import HttpResponse

import django_excel as excel
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, reverse
from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets, renderers, exceptions
from urllib.parse import urlparse, urlunparse
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventSerializer
from .models import Event
from layout.models import Layout
from django import forms

from guest.models import Guest, GuestInfo, GuestInfoField
from guest.serializers import GuestSerializer

logger = logging.getLogger(__name__)


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    template_name = None
    name = 'event'

    html = True

    def create(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_form.html'
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = self.perform_create(serializer)

            # create default fields
            default_fields = [
                'First Name', 'Last Name', 'Company', 'Email Address', 'Phone Number', 'Designation', 'Title'
            ]
            for i in range(0, len(default_fields)):
                is_email = False
                if 'Email' in default_fields[i]:
                    is_email = True
                GuestInfoField.save_guest_info_field(
                    event_id=instance,
                    field_name=default_fields[i],
                    order=i,
                    is_required=True,
                    is_unique=True,
                    is_email=is_email,
                    is_resolved=True,
                    is_hidden=False
                )

            return redirect(reverse('event-list'))
        else:
            event = serializer.data
            context = {
                'event': event,
                'user': self.request.user
            }
            return Response(context)

    def retrieve(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_detail.html'
        instance = self.get_object()
        request.session['event_id'] = instance.id
        layouts = []
        if Layout.objects.filter(event_id=instance.id).exists():
            layouts = Layout.objects.filter(event_id=instance.id).values('layout_name', 'id', 'created', 'modified')

        guest_list = Guest.objects.filter(event_id=instance.id).values('event_id', 'type', 'code', 'id')
        guest_fields = GuestInfoField.objects.filter(event_id=instance.id).exclude(is_hidden=True).values('id',
                                                                                                          'is_unique',
                                                                                                          'field_name')
        guest_infos = GuestInfo.objects.filter(event_id=instance.id).exclude(
            guest_info_field_id__is_hidden=True).values('event_id',
                                                        'guest_id',
                                                        'guest_info_field_id',
                                                        'key',
                                                        'value', 'id')

        unique_fields = GuestInfoField.objects.filter(event_id=instance.id, is_unique=True).exclude(
            is_hidden=True).values('id',
                                   'is_unique',
                                   'field_name')

        temp_dups = defaultdict(list)
        data_dups = defaultdict(list)
        count = {}
        for field in unique_fields:
            for info in guest_infos:
                if info['key'] == field['field_name']:
                    temp_dups[info['key']].append(info['value'])
                    # count = dict(Counter(temp_dups(info['key'])))
                    sample = temp_dups[info['key']]
                    count = dict(Counter(sample))
            data_dups[field['field_name']].append(count)

        dup_list = []
        for key in data_dups:
            for key, value in data_dups[key][0].items():
                id_list = []
                guest_id = GuestInfo.objects.filter(value=key).values('guest_id')
                if len(guest_id) > 1:
                    for id in guest_id:
                        id_list.append(id['guest_id'])
                    dup_list.append(id_list)

        duplicates_list = [list(item) for item in set(tuple(row) for row in dup_list)]

        serializer = self.get_serializer(instance)
        data = serializer.data
        context = {'event': data,
                   'layouts': list(layouts),
                   'guest_list': list(guest_list),
                   'guest_fields': list(guest_fields),
                   'guest_infos': list(guest_infos),
                   'duplicates_list': duplicates_list
                   }
        return Response(context)

    @detail_route(methods=['get'])
    def duplicates_list(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_duplicates.html'
        event_id = kwargs['pk']
        guest_list = Guest.objects.filter(event_id__id=event_id).values('event_id', 'type', 'code', 'id')
        unique_fields = GuestInfoField.objects.filter(event_id__id=event_id, is_unique=True).exclude(
            is_hidden=True).values('id',
                                   'is_unique',
                                   'field_name')

        guest_fields = GuestInfoField.objects.filter(event_id__id=event_id).exclude(is_hidden=True).values('id',
                                                                                                           'is_unique',
                                                                                                           'field_name')

        guest_infos = GuestInfo.objects.filter(event_id__id=event_id).exclude(
            guest_info_field_id__is_hidden=True).values('event_id',
                                                        'guest_id',
                                                        'guest_info_field_id',
                                                        'key',
                                                        'value', 'id')

        temp_dups = defaultdict(list)
        data_dups = defaultdict(list)
        count = {}
        for field in unique_fields:
            for info in guest_infos:
                if info['key'] == field['field_name']:
                    temp_dups[info['key']].append(info['value'])
                    # count = dict(Counter(temp_dups(info['key'])))
                    sample = temp_dups[info['key']]
                    count = dict(Counter(sample))
            data_dups[field['field_name']].append(count)

        dup_list = []
        for key in data_dups:
            for key, value in data_dups[key][0].items():
                id_list = []
                guest_id = GuestInfo.objects.filter(value=key).values('guest_id')
                if len(guest_id) > 1:
                    for id in guest_id:
                        id_list.append(id['guest_id'])
                    dup_list.append(id_list)

        duplicates_list = [list(item) for item in set(tuple(row) for row in dup_list)]

        guest_dup_list = []
        guest_default_dict = defaultdict(list)

        for duplicate in duplicates_list:
            for id in duplicate:
                guest_info = GuestInfo.objects.filter(guest_id__id=id).values('value', 'key', 'guest_id', 'id',
                                                                              'guest_info_field_id')
                for info in guest_info:
                    data = {
                        'value': info['value'],
                        'id': info['id'],
                        'key': info['key'],
                        'event_id': event_id,
                        'guest_id': info['guest_id'],
                        'guest_info_field_id': info['guest_info_field_id'],
                        'edit': False,
                        'checked': False
                    }
                    guest_default_dict[id].append(data)
        context = {
            'event_id': event_id,
            'guest_fields': list(guest_fields),
            'duplicates_list': duplicates_list,
            'guest_default_dict': guest_default_dict
        }
        return Response(context)

    def update(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_form.html'
        instance = Event.objects.get(id=kwargs.get('pk'))

        if 'name' not in request.data:
            serializer = self.get_serializer(instance)
            event = serializer.data
            context = {
                'event': event
            }
            response = Response(context)
        else:
            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                self.perform_update(serializer)
                response = redirect(reverse('event-detail', kwargs={'pk': kwargs['pk']}))
            else:
                event = serializer.data
                context = {
                    'event': event,
                    'user': self.request.user
                }
                response = Response(context)
        return response

    def list(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_list.html'
        response = super(EventsViewSet, self).list(request, *args, **kwargs)
        # response.data = {'results': response.data}
        response.data['user'] = self.request.user
        return response

    @detail_route(methods=['get'])
    def download_guest(self, request, *args, **kwargs):

        event_id = kwargs.get('pk')

        event = Event.objects.get(id=event_id)

        filename = event.name
        current = datetime.datetime.now()
        current = current.strftime('%Y%m%d_%H%M')

        #  file name of the downloaded excel
        filename = filename + '_' + current

        # response from site when downloading excel file
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=' + filename + '.xlsx'

        # creation of excel file body and data
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet_s = workbook.add_worksheet("Guests")
        #  body of worksheet

        guest_fields = GuestInfoField.objects.filter(event_id__id=event_id).values('field_name', 'id')
        guest_info = GuestInfo.objects.filter(event_id__id=event_id).values('guest_info_field_id', 'value', 'guest_id')

        guest = Guest.objects.filter(event_id__id=event_id).values('id')

        guest_list_info = defaultdict(list)
        for info in guest_info:
            guest_list_info[info['guest_info_field_id']].append(info['value'])

        for i in range(0, len(list(guest_fields))):
            worksheet_s.write(0, i, guest_fields[i]['field_name'])
            guest_id = guest_fields[i]['id']
            for x in range(0, len(list(guest_list_info[guest_id]))):
                if len(guest_list_info[guest_id]) > 0:
                    worksheet_s.write(x + 1, i, guest_list_info[guest_id][x])
                else:
                    worksheet_s.write(x + 1, i, '')

        workbook.close()
        output.seek(0)
        xlsx_data = output.getvalue()
        response.write(xlsx_data)
        return response

    @detail_route(methods=['post'])
    def upload_excel(self, request, *args, **kwargs):
        filename = ''
        response = ''
        if request.data['file'] != '':
            event_id = kwargs['pk']
            filename = request.data['file']
            data = get_data(filename)
            str_output = json.dumps(data).replace("/", "\\/")
            str_dict = json.loads(str_output)
            list_guests = str_dict.get('Guest List')

            event_instance = Event.objects.get(id=event_id)

            guest_info_list = []
            count = 1
            event = Event.objects.get(id=event_id)

            guest_info_fields = GuestInfoField.objects.filter(field_name__in=list_guests[0]).values('field_name')
            field_list = []
            for info in guest_info_fields:
                field_list.append(info['field_name'])

            # add fields in excel if it is not existing in the event detail
            diff_field = [x for x in list_guests[0] if x not in field_list]
            if len(diff_field) > 1:
                for field in diff_field:
                    if field != 'GuestId':
                        field_name = field
                        event_id = event_instance
                        is_required = False
                        is_unique = False
                        is_required = False
                        is_email = False
                        if 'email' in field_name.lower():
                            is_unique = True
                            is_required = True
                            is_email = True
                        is_resolved = True
                        order = len(guest_info_fields)
                        GuestInfoField.save_guest_info_field(
                            event_id=event_id,
                            field_name=field_name,
                            is_resolved=is_resolved,
                            is_unique=is_unique,
                            is_required=is_required,
                            is_email=is_email,
                            order=order
                        )

            for guest in list_guests[1:]:
                type = 'Pre Registered'
                code = guest[0]
                guest_data = {
                    'event_id': event.id,
                    'code': code,
                    'type': type
                }
                guest_serializer = self.get_serializer(data=guest_data)
                if (guest_serializer.is_valid()):
                    instance = self.perform_create(guest_serializer)
                    for x in range(0, len(list_guests[0])):
                        if (GuestInfoField.objects.filter(field_name__icontains=list_guests[0][x].strip(),
                                                          event_id=event_id).values('id').exists()):
                            guest_info_field = GuestInfoField.objects.get(
                                field_name__icontains=list_guests[0][x].strip(),
                                event_id=event_id)

                            guest = GuestInfo.save_guest_information(
                                event_id=event,
                                guest_id=instance,
                                guest_info_field=guest_info_field,
                                key=list_guests[0][x],
                                value=list_guests[count][x]
                            )
                    count += 1

                    # guest_data_list = defaultdict(list)
                    # for x in range(0, len(list_guests[0])):
                    #     for y in range(1, len(list_guests[1:])):
                    #         guest_data_list[list_guests[0][x]].append(list_guests[y][x])
                    #
                    # guest_id_list = []
                    # guest_create_list = []
                    # for z in range(0, len(list_guests) - 1):
                    #     type = 'Pre Registered'
                    #     if list_guests[z][0] != 'GuestId':
                    #         data = {
                    #             'event_id': event_instance.id,
                    #             'code': list_guests[z][0],
                    #             'type': type
                    #         }
                    #         guest_serializer = self.get_serializer(data=data)
                    #         if guest_serializer.is_valid():
                    #             instance = self.perform_create(guest_serializer)
                    #             for key in guest_data_list:
                    #                 if key != 'GuestId':
                    #                     print(key)
                    #                     print(guest_data_list[key])
                    #                     # guest_info_field = GuestInfoField.objects.get(
                    #                     #     field_name=key.strip(),
                    #                     #     event_id=event_id)
                    #                     # guest = GuestInfo.save_guest_information(
                    #                     #     event_id=event_instance,
                    #                     #     guest_id=instance,
                    #                     #     guest_info_field=guest_info_field,
                    #                     #     key=key,
                    #                     #     value=list_guests[count][x]
                    #                     # )
                    #
                    #             # for key in guest_data_list:
                    #             #                 if key != 'GuestId':
                    #             #                     g_info_id = GuestInfoField.objects.get(field_name=key.strip())
                    #             #                     for values in guest_data_list[key]:
                    #             #                         guest_info_data = {
                    #             #                             'event_id': event_instance,
                    #             #                             'guest_id': instance,
                    #             #                             'guest_info_field_id': g_info_id,
                    #             #                             'key': key,
                    #             #                             'value': values
                    #             #                         }
                    #             #                         print(guest_info_data)
                    #             #                         guest_create_list.append(guest_info_data)
                    #             # print(guest_create_list)
                    #             # print(len(guest_create_list))
                    #             # GuestInfo.save_guest_bulk_create(guest_create_list)
        return redirect(reverse('event-detail', args=kwargs['pk']))

    @list_route(methods=['get'])
    def events_list(self, request, *args, **kwargs):
        self.renderers_classes = [renderers.JSONRenderer()]
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['guest_events'])
    def guest_events(self, request, *args, **kwargs):
        event_id = None
        search = self.request.query_params.get('search')
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()
        type = 'All'
        if 'type' in self.request.query_params:
            type = self.request.query_params.get('type')

        guest_infos = GuestInfo.objects.filter(event_id=event_id, value__icontains=search.strip()).values('guest_id')
        list_guest = [info['guest_id'] for info in guest_infos]
        if type == 'All':
            guest_list = Guest.objects.filter(event_id=event_id, id__in=list_guest).values('event_id', 'type', 'code',
                                                                                           'id')
        else:
            guest_list = Guest.objects.filter(event_id=event_id, id__in=list_guest, type=type).values(
                'event_id', 'type', 'code',
                'id')

        guest_info_search = GuestInfo.objects.filter(guest_id__in=list_guest).values('event_id',
                                                                                     'guest_id',
                                                                                     'guest_info_field_id',
                                                                                     'key',
                                                                                     'value')
        context = {
            'guest_list': list(guest_list),
            'guest_infos': list(guest_info_search)
        }
        return Response(context)

    def destroy(self, request, *args, **kwargs):
        response = super(EventsViewSet, self).destroy(request, *args, **kwargs)
        response = redirect(reverse('event-list'))
        return response

    def perform_create(self, serializer):
        return serializer.save()

    def perform_update(self, serializer, **kwargs):
        serializer.save(modified_by=self.request.user, **kwargs)

    def get_renderers(self):
        if self.html:
            if self.request.path_info == '/api/events/':
                renderers_classes = [renderers.JSONRenderer()]
            elif self.request.resolver_match.url_name == 'guest_events':
                renderers_classes = [renderers.JSONRenderer()]
            elif self.request.resolver_match.url_name == 'event-upload-excel':
                renderers_classes = [renderers.JSONRenderer()]
            else:
                renderers_classes = [renderers.TemplateHTMLRenderer()]
        else:
            renderers_classes = [renderers.JSONRenderer()]
        return renderers_classes

    def get_queryset(self):
        queryset = super(EventsViewSet, self).get_queryset()
        if self.action == 'layout_list':
            # event_id = self.kwargs['pk']
            queryset = Layout.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        if request.resolver_match.url_name == self.name + '-detail':
            if '_method' in request.data and request.data['_method'] == 'delete':
                response = self.destroy(request, *args, **kwargs)
            else:
                response = self.update(request, *args, **kwargs)
        elif self.request.resolver_match.url_name == 'event-upload-excel':
            response = super(EventsViewSet, self).upload_excel(request, *args, **kwargs)
        elif self.request.resolver_match.url_name == 'guest_events':
            response = super(EventsViewSet, self).guest_events(request, *args, **kwargs)
        else:
            response = super(EventsViewSet, self).post(request, *args, **kwargs)
        return response

    def dispatch(self, request, *args, **kwargs):
        return super(EventsViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        serializer = super(EventsViewSet, self).get_serializer(*args, **kwargs)
        return serializer

    def get_serializer_class(self):
        if self.action == 'upload_excel':
            return GuestSerializer
        return self.serializer_class

    def handle_exception(self, exc):
        # If we're in HTML mode, then we want to redirect to the login page if authentication has failed.
        if isinstance(exc, (exceptions.NotAuthenticated, exceptions.AuthenticationFailed)):
            return redirect('%s?next=%s' % (settings.LOGIN_URL, self.request.path))
        return super(EventsViewSet, self).handle_exception(exc)
