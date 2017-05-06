from django import template

register = template.Library()

@register.simple_tag()
def connect_or_login(user):
    if user.is_authenticated():
        return user.username
    else:
        return "Se connecter"

@register.simple_tag()
def myurl(pic):
    lol = pic.url.split("/")
    img = lol.pop()
    return "/static/crowd/images/" + img
