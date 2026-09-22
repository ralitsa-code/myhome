from django import template

register = template.Library()

@register.filter(name='phone_format')
def phone_format(value):
    return f'{value[:4]} {value[4:7]} {value[7:]}'