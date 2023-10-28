from django import template
from ..models import Menu
from django.utils.html import format_html

register = template.Library()



@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    html = str()
    html += '<ul>'
    html = f"<li> <a href='{current_url}'>{menu_name}</a>"
    html += '</ul>'
    items = Menu.objects.select_related('parent').filter(parent__name=menu_name)
    html += '<ul>'
    for item in items:
        html += f"<li> <a href='{item.url}'>{item.name}</a>"
    html += '</ul>'
    return format_html(html)

