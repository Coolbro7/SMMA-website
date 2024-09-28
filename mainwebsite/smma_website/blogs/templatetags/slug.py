from django import template
from django.template.defaultfilters import slugify
register = template.Library()
@register.filter(name="slug")
def slug(title):
    return slugify(title)