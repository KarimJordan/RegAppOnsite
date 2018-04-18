from rest_framework import serializers
from .models import Layout, LayoutField, LayoutFieldValue
from event.models import Event


class LayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layout
        fields = '__all__'


class LayoutListSerializer(serializers.ModelSerializer):
    event_id = serializers.StringRelatedField(source='event_id.id')

    class Meta:
        model = Layout
        fields = ('id', 'layout_name', 'event_id', 'created', 'modified')


class LayoutCreateSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = Layout
        fields = ('id', 'event_id', 'background_image', 'background_color',
                  'logo', 'logo_pos_x', 'logo_pos_y', 'logo_width', 'logo_height',
                  'canvas_height', 'canvas_width', 'canvas_padding', 'canvas_background_color',
                  'canvas_opacity', 'canvas_pos_x', 'canvas_pos_y', 'button_image', 'button_color',
                  'button_opacity', 'button_text_color', 'submit_button_text', 'next_button_text',
                  'back_button_text', 'button_font_family', 'button_font_size', 'created', 'modified', 'layout_name')


class LayoutDetailSerializer(serializers.ModelSerializer):
    event_id = serializers.StringRelatedField(source='event_id.id')
    layout_fields = serializers.SerializerMethodField()

    class Meta:
        model = Layout
        fields = ('id', 'event_id', 'layout_type', 'background_image', 'background_color',
                  'layout_fields', 'logo', 'logo_pos_x', 'logo_pos_y', 'logo_width', 'logo_height',
                  'canvas_height', 'canvas_width', 'canvas_padding', 'canvas_background_color',
                  'canvas_opacity', 'canvas_pos_x', 'canvas_pos_y', 'button_image', 'button_color',
                  'button_opacity', 'button_text_color', 'submit_button_text', 'next_button_text',
                  'back_button_text', 'button_font_family', 'button_font_size', 'created', 'modified')

    @staticmethod
    def get_layout_fields(obj):
        layout_fields_list = []
        layout_fields = LayoutField.objects.filter(layout=obj.id).all()
        for field in layout_fields:
            guest_field_id = ''
            if field.field_name != 'Spacer Field':
                guest_field_id = field.guest_field.id
            field_data = {
                'id': field.id,
                'layout_id': field.layout.id,
                'guest_info_field_id': guest_field_id,
                'type': field.type,
                'height': field.height,
                'width': field.width,
                'page_num': field.page_num,
                'field_name': field.field_name,
                'order': field.order,
                'with_placeholder': field.with_placeholder,
                'font_family': field.font_family,
                'font_color': field.font_color,
                'font_size': field.font_size,
                'background_color': field.background_color,
                'opacity': field.opacity,
                'border_color': field.border_color,
                'label_color': field.label_color,
                'label_size': field.label_size,
                'label_font_family': field.label_font_family,
                'field_values': []
            }

            layout_list_values = []
            layout_values = LayoutFieldValue.objects.filter(layout_field=field.id).all().order_by('id')
            for value in layout_values:
                info_value = {
                    'id': value.id,
                    'layout_field_id': value.layout_field_id,
                    'value': value.value
                }

                layout_list_values.append(info_value)
            field_data['field_values'] = layout_list_values
            layout_fields_list.append(field_data)
        return layout_fields_list
