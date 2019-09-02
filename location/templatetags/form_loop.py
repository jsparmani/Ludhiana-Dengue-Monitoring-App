from django import template

register = template.Library()

@register.filter
def form_loop(value, arg):
    return value[arg]