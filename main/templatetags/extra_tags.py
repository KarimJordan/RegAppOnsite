import json
import logging

from django import template
from django.utils.safestring import mark_safe

from ..utils import decimal_default

logger = logging.getLogger(__name__)

register = template.Library()


@register.filter
def dictlookup(values, key):
    return values[key]


@register.filter
def jsonify(obj):
    return mark_safe(json.dumps(obj, default=decimal_default))


@register.filter
def if_dict(value, key):
    if value is None:
        return ""
    return value.get(key) or "Key '%s' not found" % key
