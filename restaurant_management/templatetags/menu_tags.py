from django import template

register = template.library()
@register.filter(name='availability')
def availablity(item):
    if not item.available:
        return f"{item.name} - Coming Soon"
    return item.name