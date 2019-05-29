import datetime
from django import template

register = template.Library()

@register.simple_tag
def hora_atual(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def hora_atual_recebe_contexto(context, format_string):
    return datetime.datetime.now().strftime(format_string)

