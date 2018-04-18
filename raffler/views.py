import logging
import itertools
import json
from collections import defaultdict
from django.shortcuts import render, redirect, reverse

# Create your views here.
from .serializers import RafflerSerializer, RafflerWinnerSerializer
from rest_framework.decorators import list_route, detail_route
from django.http import Http404
from rest_framework.response import Response
from .models import Raffler, RafflerSelectionWinner, RafflerWinner
from event.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin

from guest.models import GuestInfoField, Guest, GuestInfo

from rest_framework import viewsets, renderers

logger = logging.getLogger(__name__)


class RafflerViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = RafflerSerializer
    queryset = Raffler.objects.all()

    template_name = None
    name = 'raffler'

    def list(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_list.html'

        event_id = None
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)

        response = super(RafflerViewSet, self).list(request, *args, **kwargs)
        response.data['event_id'] = event_id
        return response

    def create(self, request, *agrs, **kwargs):
        self.template_name = self.name + '/' + self.name + '_form.html'
        event_id = None
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return redirect(reverse('raffler-list'))
        else:
            context = serializer.data
            guest_fields = GuestInfoField.objects.filter(event_id__id=event_id).values('field_name', 'id')
            context['guest_fields'] = list(guest_fields)
            context['event_id'] = event_id
            context['conditions_data'] = ''
            return Response(context)

    def destroy(self, request, *args, **kwargs):
        response = super(RafflerViewSet, self).destroy(request, *args, **kwargs)
        response = redirect(reverse('raffler-list'))
        return response

    def update(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_form.html'
        instance = self.get_object()

        event_id = None
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)

        guest_fields = GuestInfoField.objects.filter(event_id__id=event_id).values('field_name', 'id')
        guest_fields = list(guest_fields)

        if 'title' not in request.data:
            serializer = self.get_serializer(instance)
            raffle = serializer.data
            conditions_data = ''
            if raffle['conditions'] != None:
                conditions_data = json.loads(raffle['conditions'])
            context = {
                'raffle': raffle,
                'conditions_data': conditions_data,
                'event_id': event_id,
                'guest_fields': guest_fields
            }
            response = Response(context)
        else:
            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            logger.error(serializer.is_valid())
            logger.error(serializer.errors)
            if serializer.is_valid():
                self.perform_update(serializer)
                response = redirect(reverse('raffler-list'))
            else:
                raffle = serializer.data
                conditions_data = ''
                if raffle['conditions'] != None:
                    conditions_data = json.loads(raffle['conditions'])
                context = {
                    'raffle': raffle,
                    'event_id': event_id,
                    'guest_fields': guest_fields,
                    'user': self.request.user,
                    'conditions_data': conditions_data,
                }
                response = Response(context)
        return response

    @detail_route(methods=['get'])
    def search_participants(self, request, *args, **kwargs):
        instance = self.get_object()

        search = ''
        if 'search' in self.request.query_params:
            search = self.request.query_params.get('search')

        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        search_guest_ids = GuestInfo.objects.filter(value__icontains=search.strip()).values('guest_id')
        search_guest_ids = [sid['guest_id'] for sid in search_guest_ids]

        guests = Guest.objects.filter(id__in=search_guest_ids).values('id')

        guest_infos = GuestInfo.objects.filter(guest_id__in=[guest['id'] for guest in guests]).values('value', 'key',
                                                                                                      'guest_id')
        guest_info_default_dict = defaultdict(list)
        for info in guest_infos:
            guest_info_default_dict[info['guest_id']].append(info['value'])

        # guest_list = []
        # for guest in guests:
        #     guest_data = guest_info_default_dict[guest['id']]
        #     guest_list.append(guest_data)

        raffle_winners = RafflerWinner.objects.filter(raffle__id=instance.id).values('guest__id')

        excluded_guest = []
        included_guest = [gid['id'] for gid in guests]

        conditions_data = ''
        if instance.conditions != '':
            conditions_data = json.loads(instance.conditions)

        for condition in conditions_data:
            if condition['selected_filter'] == 'Include':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['value'] == condition['selected_value']:
                            if info['guest_id'] in excluded_guest:
                                excluded_guest.remove(info['guest_id'])
            elif condition['selected_filter'] == 'Exclude':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['value'] == condition['selected_value']:
                            excluded_guest.append(info['guest_id'])
            elif condition['selected_filter'] == 'Include Specific':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['guest_id'] not in excluded_guest:
                            excluded_guest.append(info['guest_id'])
                        if info['value'] == condition['selected_value']:
                            if info['guest_id'] in excluded_guest:
                                excluded_guest.remove(info['guest_id'])
            elif condition['selected_filter'] == 'Exclude Specific':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['value'] == condition['selected_value']:
                            included_guest.remove(info['guest_id'])

        for eid in excluded_guest:
            if eid in included_guest:
                included_guest.remove(eid)

        logger.error(raffle_winners)

        for winner in raffle_winners:
            if winner['guest__id'] in included_guest:
                logger.error('lkjklk')
                included_guest.remove(winner['guest__id'])

        logger.error(included_guest)

        guest_info_default_dict = defaultdict(list)
        sample = defaultdict(list)
        for info in guest_infos:
            data = {
                'key': info['key'],
                'value': info['value']
            }
            sample[info['guest_id']].append(data)
            guest_info_default_dict[info['guest_id']].append(info['value'])

        guest_list = []
        for guest in included_guest:
            guest_data = guest_info_default_dict[guest]
            guest_list.append(guest_data)

        context = {
            'guest_list': guest_list,
            'event_id': instance.event.id,
            'raffle_id': kwargs.get('pk')
        }
        return Response(context)

    @detail_route(methods=['get'])
    def search_winners(self, request, *args, **kwargs):
        instance = self.get_object()

        search = ''
        if 'search' in self.request.query_params:
            search = self.request.query_params.get('search')

        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        search_guest_ids = GuestInfo.objects.filter(value__icontains=search.strip()).values('guest_id')
        search_guest_ids = [sid['guest_id'] for sid in search_guest_ids]

        raffle_winner = RafflerWinner.objects.filter(raffle=instance, guest__id__in=search_guest_ids).values(
            'guest__id')

        guest_ids = [winner['guest__id'] for winner in raffle_winner]
        guests = Guest.objects.filter(id__in=guest_ids).values('id')

        guest_infos = GuestInfo.objects.filter(guest_id__in=[guest['id'] for guest in guests]).values('value', 'key',
                                                                                                      'guest_id')

        guest_info_default_dict = defaultdict(list)
        for info in guest_infos:
            guest_info_default_dict[info['guest_id']].append(info['value'])

        winner_list = []
        for winner in raffle_winner:
            winner_data = guest_info_default_dict[winner['guest__id']]
            winner_list.append(winner_data)

        context = {
            'winner_list': winner_list,
            'event_id': instance.event.id,
            'raffle_id': kwargs.get('pk')
        }
        return Response(context)

    @detail_route(methods=['get'])
    def raffle_winners(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_winners.html'

        instance = self.get_object()

        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        raffle_winner = RafflerWinner.objects.filter(raffle=instance).values('guest__id')
        guest_ids = [winner['guest__id'] for winner in raffle_winner]
        guests = Guest.objects.filter(id__in=guest_ids).values('id')

        guest_infos = GuestInfo.objects.filter(guest_id__in=[guest['id'] for guest in guests]).values('value', 'key',
                                                                                                      'guest_id')
        guest_info_default_dict = defaultdict(list)
        for info in guest_infos:
            guest_info_default_dict[info['guest_id']].append(info['value'])

        winner_list = []
        for winner in raffle_winner:
            winner_data = guest_info_default_dict[winner['guest__id']]
            winner_list.append(winner_data)

        guest_fields = GuestInfoField.objects.filter(event_id__id=event_id).values('field_name').order_by('order')
        guest_fields = list(guest_fields)

        context = {
            'guest_fields': guest_fields,
            'winner_list': winner_list,
            'event_id': instance.event.id,
            'raffle_id': kwargs.get('pk')
        }
        return Response(context)

    @detail_route()
    def raffle_participants(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_participant.html'
        instance = self.get_object()

        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        conditions_data = ''
        if instance.conditions != '':
            conditions_data = json.loads(instance.conditions)

        guests = Guest.objects.filter(event_id=event_id).values('id')
        guest_infos = GuestInfo.objects.filter(guest_id__in=[guest['id'] for guest in guests]).values('value', 'key',
                                                                                                      'guest_id')

        raffle_winners = RafflerWinner.objects.filter(raffle__id=instance.id).values('guest__id')

        excluded_guest = []
        included_guest = [gid['id'] for gid in guests]

        for condition in conditions_data:
            if condition['selected_filter'] == 'Include':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['value'] == condition['selected_value']:
                            if info['guest_id'] in excluded_guest:
                                excluded_guest.remove(info['guest_id'])
            elif condition['selected_filter'] == 'Exclude':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['value'] == condition['selected_value']:
                            excluded_guest.append(info['guest_id'])
            elif condition['selected_filter'] == 'Include Specific':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['guest_id'] not in excluded_guest:
                            excluded_guest.append(info['guest_id'])
                        if info['value'] == condition['selected_value']:
                            if info['guest_id'] in excluded_guest:
                                excluded_guest.remove(info['guest_id'])
            elif condition['selected_filter'] == 'Exclude Specific':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['value'] == condition['selected_value']:
                            included_guest.remove(info['guest_id'])

        for eid in excluded_guest:
            if eid in included_guest:
                included_guest.remove(eid)

        logger.error(raffle_winners)

        for winner in raffle_winners:
            if winner['guest__id'] in included_guest:
                logger.error('lkjklk')
                included_guest.remove(winner['guest__id'])

        logger.error(included_guest)

        guest_info_default_dict = defaultdict(list)
        sample = defaultdict(list)
        for info in guest_infos:
            data = {
                'key': info['key'],
                'value': info['value']
            }
            sample[info['guest_id']].append(data)
            guest_info_default_dict[info['guest_id']].append(info['value'])

        guest_list = []
        for guest in included_guest:
            guest_data = guest_info_default_dict[guest]
            guest_list.append(guest_data)

        logger.error(guest_list)

        guest_fields = GuestInfoField.objects.filter(event_id__id=event_id).values('field_name').order_by('order')
        guest_fields = list(guest_fields)

        context = {
            'guest_list': guest_list,
            'guest_fields': guest_fields,
            'event_id': instance.event.id,
            'raffle_id': kwargs.get('pk')
        }
        return Response(context)

    @detail_route(methods=['post'])
    def copy_raffle(self, request, *args, **kwargs):
        copied_raffle = kwargs.get('pk')
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()
        raffle_instance = Raffler.objects.get(id=copied_raffle)
        data = {
            'event': raffle_instance.event,
            'title': 'Copy ' + raffle_instance.title,
            'num_of_draws': raffle_instance.num_of_draws,
            'num_of_draws_done': raffle_instance.num_of_draws_done,
            'label': raffle_instance.label,
            'draw_duration': raffle_instance.draw_duration,
            'item_duration': raffle_instance.item_duration,
            'prize_image': raffle_instance.prize_image,
            'background_image': raffle_instance.background_image,
            'conditions': raffle_instance.conditions
        }
        Raffler.copy_raffle(data)
        response = super(RafflerViewSet, self).list(request, *args, **kwargs)
        response.data['event_id'] = event_id
        return response

    @detail_route(methods=['get'])
    def play_raffle(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_play.html'
        event_id = None
        raffle_id = kwargs.get('pk')

        instance = self.get_object()

        serializer = self.get_serializer(instance)
        data = serializer.data

        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        guest_id = Guest.objects.filter(event_id__id=event_id).values('id').order_by('id')
        guest_id = list(guest_id)

        guest_infos = GuestInfo.objects.filter(event_id__id=event_id).values('value', 'key', 'guest_id').order_by(
            'guest_id')

        guest_info_default_dict = defaultdict(list)
        for info in guest_infos:
            guest_info_default_dict[info['guest_id']].append(info)

        #

        conditions_data = ''
        if instance.conditions != '':
            conditions_data = json.loads(instance.conditions)

        raffle_winners = RafflerWinner.objects.filter(id=raffle_id).values('guest__id')

        excluded_guest = []
        included_guest = [gid['id'] for gid in guest_id]

        for condition in conditions_data:
            if condition['selected_filter'] == 'Include':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['value'] == condition['selected_value']:
                            excluded_guest.remove(info['guest_id'])
            elif condition['selected_filter'] == 'Exclude':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['value'] == condition['selected_value']:
                            excluded_guest.append(info['guest_id'])
            elif condition['selected_filter'] == 'Include Specific':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['guest_id'] not in excluded_guest:
                            excluded_guest.append(info['guest_id'])
                        if info['value'] == condition['selected_value']:
                            excluded_guest.remove(info['guest_id'])
            elif condition['selected_filter'] == 'Exclude Specific':
                for info in guest_infos:
                    if info['key'] == condition['selected_field']:
                        if info['value'] == condition['selected_value']:
                            included_guest.remove(info['guest_id'])

        for eid in excluded_guest:
            included_guest.remove(eid)

        for winner in raffle_winners:
            included_guest.remove(winner['guest__id'])

        list_name = []
        sample = []
        for guest in [gid for gid in included_guest]:
            name = ''
            for info in guest_info_default_dict[guest]:
                if info['key'] == 'First Name':
                    name += info['value']
                    name += ' '
                if info['key'] == 'Last Name':
                    name += info['value']
                    rdata = {
                        'name': name,
                        'gid': info['guest_id']
                    }
                    sample.append(rdata)
                    list_name.append(name)

        list_sample = [name['name'] for name in sample]
        list_id = [gid['gid'] for gid in sample]

        context = {
            'raffle': data,
            'guest_id': list_id,
            'name_list': list_sample
        }
        return Response(context)

    @detail_route(methods=['post'])
    def save_winner(self, request, *args, **kwargs):
        event_id = None
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        raffler_id = kwargs.get('pk')
        serializer = self.get_serializer(data=request.data)

        print(request.data)

        if 'winner_id' in request.data:
            winner_name = request.data['winner_name']
            winner_id = request.data['winner_id']
            draws = request.data['draws']

            guest = Guest.objects.filter(id=winner_id)
            guest_info = GuestInfo.objects.filter(guest_id__id=winner_id).values('value', 'key', 'guest_id')

            first_name = ''
            last_name = ''

            for info in guest_info:
                if info['key'] == 'First Name':
                    first_name = info['value']
                if info['key'] == 'Last Name':
                    last_name = info['value']

            guest_info_id = GuestInfo.objects.filter(value__in=[first_name, last_name]).values('guest_id')

            id_list = []
            id_list.append(int(winner_id))
            for giid in guest_info_id:
                id_list.append(giid['guest_id'])

            id_list = list(set(id_list))
            for id in id_list:
                context = {
                    'raffle': raffler_id,
                    'guest': id
                }
                serializer = self.get_serializer(data=context)
                if serializer.is_valid():
                    self.perform_create(serializer)

            raffle_instance = Raffler.objects.get(id=raffler_id)
            raffle_instance.num_of_draws_done = int(draws)
            raffle_instance.save()

            conditions_data = ''
            if raffle_instance.conditions != '':
                conditions_data = json.loads(raffle_instance.conditions)

            raffle_data = {
                'id': raffle_instance.id,
                'title': raffle_instance.title,
                'num_of_draws': raffle_instance.num_of_draws,
                'label': raffle_instance.label,
                'num_of_draws_done': raffle_instance.num_of_draws_done,
                'draw_duration': raffle_instance.draw_duration,
                'item_duration': raffle_instance.item_duration,
                'prize_image': raffle_instance.prize_image,
                'background_image': raffle_instance.background_image,
                'conditions': raffle_instance.conditions
            }

            context = {
                'raffle': raffle_data,
                'conditions_data': conditions_data
            }
            return Response(context)

        else:
            context = serializer.data
            guest_fields = GuestInfoField.objects.filter(event_id__id=event_id).values('field_name', 'id')
            context['guest_fields'] = list(guest_fields)
            context['event_id'] = event_id
            context['conditions_data'] = ''
            return Response(context)

    @list_route(methods=['get'])
    def field_value_list(self, request, *args, **kwargs):

        event_id = None
        selected_field = self.request.query_params.get('selected_field')
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        guest_infos = GuestInfo.objects.filter(event_id=event_id,
                                               key=selected_field.strip()).values('value')
        guest_infos = [i for n, i in enumerate(guest_infos) if i not in guest_infos[n + 1:]]
        context = {
            'guest_infos': list(guest_infos)
        }
        return Response(context)

    def post(self, request, *args, **kwargs):
        logger.error(request.data)
        if request.resolver_match.url_name == self.name + '-detail':
            if '_method' in request.data and request.data['_method'] == 'delete':
                response = self.destroy(request, *args, **kwargs)
            else:
                response = self.update(request, *args, **kwargs)
        else:
            response = super(RafflerViewSet, self).post(request, *args, **kwargs)
        return response

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'save_winner':
            return RafflerWinnerSerializer
        return self.serializer_class

    def get_renderers(self):
        # print()
        if self.request.resolver_match.url_name == 'field_value_list':
            renderer_class = [renderers.JSONRenderer()]
        elif self.request.resolver_match.url_name == 'raffler-copy-raffle':
            renderer_class = [renderers.JSONRenderer()]
        elif self.request.resolver_match.url_name == 'raffler-play-raffle':
            renderer_class = [renderers.TemplateHTMLRenderer()]
        elif self.request.resolver_match.url_name == 'raffler-search-winners':
            renderer_class = [renderers.JSONRenderer()]
        elif self.request.resolver_match.url_name == 'raffler-search-participants':
            renderer_class = [renderers.JSONRenderer()]
        elif self.request.resolver_match.url_name == 'raffler-save-winner':
            renderer_class = [renderers.JSONRenderer()]
        else:
            renderer_class = [renderers.TemplateHTMLRenderer()]
        return renderer_class

    def get_queryset(self):
        queryset = super(RafflerViewSet, self).get_queryset()
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
            queryset = queryset.filter(event__id=event_id)
        return queryset
