from django.template import Library
from utils.real import format_price_real
from utils.cart_total import cart_total_quantity
from utils.cart_totals import carts_to


register = Library()

@register.filter
def format_price(value):
    return format_price_real(value)


@register.filter
def cart_total(cart):
    return cart_total_quantity(cart)


@register.filter
def cart_totals(cart):
    return carts_to(cart)
