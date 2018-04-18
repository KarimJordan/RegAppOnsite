from django.db import models
from event.models import Event
from guest.models import GuestInfoField


class Layout(models.Model):
    layout_name = models.CharField(max_length=200)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    layout_type = models.IntegerField(default=0)
    background_image = models.TextField(null=True, blank=True)
    background_color = models.CharField(max_length=200, null=True, blank=True)
    logo = models.TextField(null=True, blank=True)
    logo_pos_x = models.CharField(max_length=200, null=True, blank=True)
    logo_pos_y = models.CharField(max_length=200, null=True, blank=True)
    logo_width = models.CharField(max_length=200, null=True, blank=True)
    logo_height = models.CharField(max_length=200, null=True, blank=True)
    canvas_height = models.CharField(max_length=200)
    canvas_width = models.CharField(max_length=200)
    canvas_padding = models.CharField(max_length=200)
    canvas_background_color = models.CharField(max_length=200)
    canvas_opacity = models.CharField(max_length=200)
    canvas_pos_x = models.CharField(max_length=200)
    canvas_pos_y = models.CharField(max_length=200)
    button_image = models.CharField(max_length=200, null=True, blank=True)
    button_color = models.CharField(max_length=20)
    button_opacity = models.CharField(max_length=200)
    button_text_color = models.CharField(max_length=200)
    submit_button_text = models.CharField(max_length=200)
    next_button_text = models.CharField(max_length=200)
    back_button_text = models.CharField(max_length=200)
    button_font_family = models.CharField(max_length=50)
    button_font_size = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.layout_name


class LayoutField(models.Model):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    guest_field = models.ForeignKey(GuestInfoField, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    width = models.CharField(max_length=200)
    field_name = models.CharField(max_length=200)
    order = models.CharField(max_length=200)
    with_placeholder = models.BooleanField(default=True)
    font_family = models.CharField(max_length=200)
    font_color = models.CharField(max_length=100)
    font_size = models.CharField(max_length=200)
    background_color = models.CharField(max_length=100)
    opacity = models.CharField(max_length=200)
    border_color = models.CharField(max_length=100)
    label_color = models.CharField(max_length=100)
    label_size = models.CharField(max_length=200)
    page_num = models.CharField(max_length=200)
    label_font_family = models.CharField(default='Arial', max_length=100)
    list_font_color = models.CharField(max_length=100, null=True, blank=True)
    list_font_family = models.CharField(max_length=100, null=True, blank=True)
    list_font_size = models.CharField(max_length=100, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.layout.layout_name + ' : ' + self.field_name

    @staticmethod
    def save_layout_field(layout_fields_data, layout_id):
        if type(layout_fields_data) is dict:
            layout_instance = Layout.objects.get(id=layout_id)
            if layout_fields_data['field_name'] != 'Spacer Field':
                guest_field = GuestInfoField.objects.get(id=int(layout_fields_data['guest_info_field_id']))
                layout_field = LayoutField(
                    layout=layout_instance,
                    guest_field=guest_field,
                    type=layout_fields_data['type'],
                    height=layout_fields_data['height'],
                    width=layout_fields_data['width'],
                    field_name=layout_fields_data['field_name'],
                    order=layout_fields_data['order'],
                    with_placeholder=layout_fields_data['with_placeholder'],
                    font_family=layout_fields_data['font_family'],
                    font_color=layout_fields_data['font_color'],
                    font_size=layout_fields_data['font_size'],
                    background_color=layout_fields_data['background_color'],
                    opacity=layout_fields_data['opacity'],
                    border_color=layout_fields_data['border_color'],
                    label_color=layout_fields_data['label_color'],
                    label_size=layout_fields_data['label_size'],
                    label_font_family=layout_fields_data['label_font_family'],
                    page_num=layout_fields_data['page_num'],
                    list_font_color=layout_fields_data['list_font_color'],
                    list_font_family=layout_fields_data['list_font_family'],
                    list_font_size=layout_fields_data['list_font_size']
                )
                layout_field.save()
                layout_values = layout_fields_data['field_values']
                if len(layout_values) > 1:
                    for layout_value in layout_values:
                        layout_field_value = LayoutFieldValue(
                            value=layout_value,
                            layout_field=layout_field
                        )
                        layout_field_value.save()
            else:
                layout_field = LayoutField(
                    layout=layout_instance,
                    type=layout_fields_data['type'],
                    height=layout_fields_data['height'],
                    width=layout_fields_data['width'],
                    field_name=layout_fields_data['field_name'],
                    order=layout_fields_data['order'],
                    with_placeholder=layout_fields_data['with_placeholder'],
                    font_family=layout_fields_data['font_family'],
                    font_color=layout_fields_data['font_color'],
                    font_size=layout_fields_data['font_size'],
                    background_color=layout_fields_data['background_color'],
                    opacity=layout_fields_data['opacity'],
                    border_color=layout_fields_data['border_color'],
                    label_color=layout_fields_data['label_color'],
                    label_size=layout_fields_data['label_size'],
                    label_font_family=layout_fields_data['label_font_family'],
                    page_num=layout_fields_data['page_num'],
                    list_font_color=layout_fields_data['list_font_color'],
                    list_font_family=layout_fields_data['list_font_family'],
                    list_font_size=layout_fields_data['list_font_size']
                )
                layout_field.save()
                layout_values = layout_fields_data['field_values']
                if len(layout_values) > 1:
                    for layout_value in layout_values:
                        layout_field_value = LayoutFieldValue(
                            value=layout_value,
                            layout_field=layout_field
                        )
                        layout_field_value.save()
        else:
            for layout_field_data in layout_fields_data:
                layout_instance = Layout.objects.get(id=layout_id)
                if layout_fields_data['field_name'] != 'Spacer Field':
                    guest_field = GuestInfoField.objects.get(id=int(layout_fields_data['guest_info_field_id']))
                    layout_field = LayoutField(
                        layout=layout_instance,
                        guest_field=guest_field,
                        type=layout_fields_data['type'],
                        height=layout_fields_data['height'],
                        width=layout_fields_data['width'],
                        field_name=layout_fields_data['field_name'],
                        order=layout_fields_data['order'],
                        with_placeholder=layout_fields_data['with_placeholder'],
                        font_family=layout_fields_data['font_family'],
                        font_color=layout_fields_data['font_color'],
                        font_size=layout_fields_data['font_size'],
                        background_color=layout_fields_data['background_color'],
                        opacity=layout_fields_data['opacity'],
                        border_color=layout_fields_data['border_color'],
                        label_color=layout_fields_data['label_color'],
                        label_size=layout_fields_data['label_size'],
                        label_font_family=layout_fields_data['label_font_family'],
                        page_num=layout_fields_data['page_num'],
                        list_font_color=layout_fields_data['list_font_color'],
                        list_font_family=layout_fields_data['list_font_family'],
                        list_font_size=layout_fields_data['list_font_size']
                    )
                    layout_field.save()
                    layout_values = layout_fields_data['field_values']
                    if len(layout_values) > 1:
                        for layout_value in layout_values:
                            layout_field_value = LayoutFieldValue(
                                value=layout_value,
                                layout_field=layout_field
                            )
                            layout_field_value.save()
                else:
                    layout_field = LayoutField(
                        layout=layout_instance,
                        type=layout_fields_data['type'],
                        height=layout_fields_data['height'],
                        width=layout_fields_data['width'],
                        field_name=layout_fields_data['field_name'],
                        order=layout_fields_data['order'],
                        with_placeholder=layout_fields_data['with_placeholder'],
                        font_family=layout_fields_data['font_family'],
                        font_color=layout_fields_data['font_color'],
                        font_size=layout_fields_data['font_size'],
                        background_color=layout_fields_data['background_color'],
                        opacity=layout_fields_data['opacity'],
                        border_color=layout_fields_data['border_color'],
                        label_color=layout_fields_data['label_color'],
                        label_size=layout_fields_data['label_size'],
                        label_font_family=layout_fields_data['label_font_family'],
                        page_num=layout_fields_data['page_num'],
                        list_font_color=layout_fields_data['list_font_color'],
                        list_font_family=layout_fields_data['list_font_family'],
                        list_font_size=layout_fields_data['list_font_size']
                    )
                    layout_field.save()
                    layout_values = layout_fields_data['field_values']
                    if len(layout_values) > 1:
                        for layout_value in layout_values:
                            layout_field_value = LayoutFieldValue(
                                value=layout_value,
                                layout_field=layout_field
                            )
                            layout_field_value.save()


class LayoutFieldValue(models.Model):
    layout_field = models.ForeignKey(LayoutField, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.layout_field.layout.layout_name + ' : ' + self.value

    @staticmethod
    def save_layout_field_value(field_data):
        layout_field = LayoutField.objects.get(id=field_data['layout_id'])
        layout_field_value = LayoutFieldValue(
            layout_field=layout_field,
            value=field_data['value']
        )
        layout_field_value.save()
