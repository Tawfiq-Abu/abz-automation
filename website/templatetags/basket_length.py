from django import template

register = template.Library()

@register.filter
def basket_length(basket):
    product_order_count = sum(product_order['quantity'] for product_order in basket["product_orders"].values())
    service_request_count = len(basket["service_requests"])
    return product_order_count + service_request_count