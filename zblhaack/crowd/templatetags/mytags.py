from django import template

register = template.Library()

@register.simple_tag()
def connect_or_login(user):
    if user.is_authenticated():
        return user.username
    else:
        return "Se connecter"
