from django import template

register = template.Library()


@register.simple_tag
def site_url(site, val):
    return site.get_right_url(val)
