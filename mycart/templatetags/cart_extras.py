from django import template

register = template.Library()

@register.filter
def get_field(form, product):
    return form[f'product_{product.id}']
