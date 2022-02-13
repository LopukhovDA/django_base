from django import template
from django.conf import settings

register = template.Library()


@register.filter(name="pieces")
def pieces(string):
    return f"{string} шт."


@register.filter(name="rubles")
def rubles(string):
    return f"{string} руб."
