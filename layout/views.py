import logging

from django.shortcuts import render, redirect
from rest_framework import viewsets, renderers, status
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse

from .serializers import LayoutSerializer, LayoutListSerializer, LayoutDetailSerializer, LayoutCreateSerializer
from .models import Layout, LayoutField, LayoutFieldValue

from guest.models import GuestInfoField

logger = logging.getLogger(__name__)


# Create your views here.
class LayoutViewSet(viewsets.ModelViewSet):
    serializer_class = LayoutSerializer
    queryset = Layout.objects.all()

    template_name = None
    name = 'layout'

    def update(self, request, *args, **kwargs):
        print('update')
        self.template_name = self.name + '/' + self.name + '_form.html'
        instance = self.get_object()

        event_id = None
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        if 'layout_name' not in request.data:
            serializer = self.get_serializer(instance)
            layout = serializer.data

            # guest_info_fields = GuestInfoField.objects.filter(event_id=event_id).order_by('order').values(
            #     'field_name',
            #     'order',
            #     'id',
            #     'is_hidden',
            #     'is_required',
            #     'is_unique',
            #     'is_email',
            #     'is_resolved')
            # guest_info_fields = list(guest_info_fields)
            guest_fields = GuestInfoField.objects.filter(event_id=event_id).order_by('order').values('field_name')
            guest_field_name_list = [g_field['field_name'] for g_field in guest_fields]

            layout_fields = LayoutField.objects.filter(layout__id=instance.id).order_by('order').values(
                'field_name', 'type', 'width', 'with_placeholder', 'font_family', 'font_color',
                'order', 'font_size', 'background_color', 'opacity', 'border_color', 'label_color',
                'label_size', 'page_num', 'label_font_family', 'list_font_color', 'list_font_family',
                'list_font_size', 'id'
            )

            layout_field_names_list = [l_field['field_name'] for l_field in layout_fields]

            diff_name = list(set(guest_field_name_list) - set(layout_field_names_list))

            removed_fields = GuestInfoField.objects.filter(event_id=event_id, field_name__in=diff_name).order_by(
                'order').values('field_name',
                                'order')

            layout_fields = list(layout_fields)
            removed_fields = list(removed_fields)
            guest_fields = list(guest_fields)

            context = {
                'layout': layout,
                'user': self.request.user,
                'guest_info_fields': layout_fields,
                'event_id': event_id,
                'removed_fields': removed_fields
            }
            response = Response(context)
        else:
            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                self.perform_update(serializer)

                layout_fields = request.data['layout_fields']
                print(layout_fields)
                layout_id = instance.id

                # remove fields
                current_fields = LayoutField.objects.filter(layout__id=layout_id).values('id')
                current_fields_id = [field['id'] for field in current_fields]

                # update ordering
                updated_field_ids = []
                for field in layout_fields:
                    if LayoutField.objects.filter(layout__id=layout_id, field_name=field['field_name']).exists():
                        layout_field_instance = LayoutField.objects.get(layout__id=layout_id,
                                                                        field_name=field['field_name'])
                        updated_field_ids.append(layout_field_instance.id)
                        layout_field_instance.order = field['order']
                        layout_field_instance.type = field['type']
                        layout_field_instance.width = field['width']
                        layout_field_instance.with_placeholder = bool(field['with_placeholder'])
                        layout_field_instance.font_family = field['font_family']
                        layout_field_instance.font_color = field['font_color']
                        layout_field_instance.font_size = field['font_size']
                        layout_field_instance.background_color = field['background_color']
                        layout_field_instance.opacity = field['opacity']
                        layout_field_instance.border_color = field['border_color']
                        layout_field_instance.label_color = field['label_color']
                        layout_field_instance.label_size = field['label_size']
                        layout_field_instance.label_font_family = field['label_font_family']
                        layout_field_instance.list_font_color = field['list_font_color']
                        layout_field_instance.list_font_family = field['list_font_family']
                        layout_field_instance.list_font_size = field['list_font_size']
                        layout_field_instance.save()
                    else:
                        print(field['field_name'] != 'Spacer Field')

                        if field['field_name'] != 'Spacer Field':
                            print(field['field_name'])
                            guest_instance = GuestInfoField.objects.get(field_name=field['field_name'])
                            field['guest_info_field_id'] = guest_instance.id
                        else:
                            field['guest_info_field_id'] = ''
                        LayoutField.save_layout_field(field, layout_id)

                diff_list = list(set(current_fields_id) - set(updated_field_ids))
                for diff_id in diff_list:
                    field_instance = LayoutField.objects.get(id=diff_id)
                    field_instance.delete()

                response = redirect(reverse('event-detail', kwargs={'pk': event_id}))
            else:
                layout = serializer.data

                guest_fields = GuestInfoField.objects.filter(event_id=event_id).order_by('order').values('field_name')
                guest_field_name_list = [g_field['field_name'] for g_field in guest_fields]

                layout_fields = LayoutField.objects.filter(layout__id=instance.id).order_by('order').values(
                    'field_name',
                    'order'
                )

                layout_field_names_list = [l_field['field_name'] for l_field in layout_fields]

                diff_name = list(set(guest_field_name_list) - set(layout_field_names_list))

                removed_fields = GuestInfoField.objects.filter(event_id=event_id, field_name__in=diff_name).order_by(
                    'order').values('field_name',
                                    'order')

                layout_fields = list(layout_fields)
                removed_fields = list(removed_fields)

                context = {
                    'layout': layout,
                    'user': self.request.user,
                    'guest_info_fields': layout_fields,
                    'event_id': event_id,
                    'removed_fields': removed_fields
                }

                response = Response(context)
        return response

    def destroy(self, request, *args, **kwargs):
        event_id = None
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()
        response = super(LayoutViewSet, self).destroy(request, *args, **kwargs)
        response = redirect(reverse('event-detail', kwargs={'pk': event_id}))
        return response

    def create(self, request, *agrs, **kwargs):
        self.template_name = self.name + '/' + self.name + '_form.html'

        event_id = None
        if hasattr(self.request, 'session'):
            event_id = self.request.session.get('event_id', None)
        if event_id is None:
            return Http404()

        # init of serialization
        serializer = self.get_serializer(data=request.data)
        if 'layout_data' in request.data:
            data_request = request.data['layout_data']
            serializer = self.get_serializer(data=data_request)
        # creation of data and formation of data to be used
        if serializer.is_valid():
            instance = self.perform_create(serializer)
            layout_id = instance.id
            # insert save to layoutfield here
            layout_field_data = request.data['layout_fields']
            LayoutField.save_layout_field(layout_field_data, layout_id)
            data = {
                'id': layout_id
            }
            headers = self.get_success_headers(serializer.data)
            response = redirect(reverse('event-detail', kwargs={'pk': event_id}))
            return response
        else:
            layout = serializer.data
            event_id = None
            if hasattr(self.request, 'session'):
                event_id = self.request.session.get('event_id', None)
            if event_id is None:
                return Http404()
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
                'layout': layout,
                'guest_info_fields': guest_info_fields,
                'event_id': event_id,
                'removed_fields': ''
            }
            return Response(context)

    @detail_route(methods=['get'])
    def layout_data(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data)

    @list_route(methods=['get'])
    def layout_list(self, request, *args, **kwargs):
        self.renderers_classes = [renderers.JSONRenderer()]
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save()

    def retrieve(self, request, *args, **kwargs):
        self.template_name = self.name + '/' + self.name + '_detail.html'

    def get_serializer(self, *args, **kwargs):
        serializer = super(LayoutViewSet, self).get_serializer(*args, **kwargs)
        return serializer

    def get_serializer_class(self):
        if self.action == 'layout_list':
            return LayoutListSerializer
        elif self.action == 'create':
            return LayoutCreateSerializer
        elif self.action == 'layout_data':
            return LayoutDetailSerializer
        return self.serializer_class

    def post(self, request, *args, **kwargs):
        if request.resolver_match.url_name == self.name + '-detail':
            if '_method' in request.data and request.data['_method'] == 'delete':
                response = self.destroy(request, *args, **kwargs)
            elif '_method' in request.data and request.data['_method'] == 'create':
                response = self.create(request, *args, **kwargs)
            else:
                response = self.update(request, *args, **kwargs)
        else:
            response = super(LayoutViewSet, self).post(request, *args, **kwargs)
        return response

    def get_queryset(self):
        queryset = super(LayoutViewSet, self).get_queryset()
        if self.action == 'layout_list':
            event_id = self.kwargs['pk']
            queryset = Layout.objects.filter(event_id=event_id).all()
        elif self.action == 'layout_data':
            layout_id = self.kwargs['pk']
            queryset = Layout.objects.filter(id=int(layout_id)).all()
        return queryset

    def get_renderers(self):
        if self.action == 'layout_list':
            renderers_classes = [renderers.JSONRenderer()]
        elif self.action == 'layout_data':
            renderers_classes = [renderers.JSONRenderer()]
        else:
            renderers_classes = [renderers.TemplateHTMLRenderer()]
        return renderers_classes

    def dispatch(self, request, *args, **kwargs):
        return super(LayoutViewSet, self).dispatch(request, *args, **kwargs)
