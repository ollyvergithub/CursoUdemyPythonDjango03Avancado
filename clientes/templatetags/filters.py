from django import template

register = template.Library()

@register.filter
def meu_filtro(data):
    return data + ' - ' + ' Alterado pelo Filter'

@register.filter
def arredonda(value, casas):
    return round(value, casas)