from django.template import Library
from utils.real import format_price_real

register = Library()

@register.filter
def format_price(value):
    return format_price_real(value)