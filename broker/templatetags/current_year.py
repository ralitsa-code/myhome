from django import template
from datetime import date

register = template.Library()

@register.simple_tag(name='current_year')
def current_year():
    return date.today().year