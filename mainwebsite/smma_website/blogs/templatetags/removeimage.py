from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()
@register.filter(name="remove_image")
@stringfilter
def remove_image(body):
    start = 0
    end = 0
    if "<p><img" in body:
        start = body.index("<p><img")
    else:
        start = -99
    if "</p>" in body[start:]:
        end = body[start:].index("</p>")
    if start != -99:
        body = body.replace(body[start:end+4],"")
    
    return body