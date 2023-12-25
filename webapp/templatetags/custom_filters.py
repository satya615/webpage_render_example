# demoapp/custom_filters.py

from django import template

register = template.Library()

@register.filter
def get_item(iterable, index):
    try:
        return iterable[index]
    except (IndexError, KeyError):
        return None



@register.filter
def calculate_index(i):
    return int((i / 10))

@register.filter
def calculate_amount(i):
    return int((i / 100))


@register.filter
def subtract_one(value):
    return value - 1

