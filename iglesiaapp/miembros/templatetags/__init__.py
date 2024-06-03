# templatetags/__init__.py

from django import template
from miembros.views import es_administrador

register = template.Library()

@register.filter(name='es_administrador')
def es_administrador_filter(user):
    return es_administrador(user)
