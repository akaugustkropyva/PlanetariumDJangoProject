from django import template

register = template.Library()

@register.filter
def getlist_filter(query_dict, key):
    return query_dict.getlist(key)