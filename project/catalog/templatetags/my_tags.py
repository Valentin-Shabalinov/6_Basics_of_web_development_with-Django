from django import template

register = template.Library()


@register.filter()
def mediapath(format_string):
    if format_string:
        return f'/media/{format_string}'
    return '#'


@register.simple_tag
def mediapath(format_string):
    if format_string:
        return f'/media/{format_string}'
    return '#'
