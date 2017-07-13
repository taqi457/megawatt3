from django import template

register = template.Library()


@register.filter(name='startswith')
def startswith(text, starts):
    if isinstance(text, basestring):
        return text.startswith(starts)
    return False