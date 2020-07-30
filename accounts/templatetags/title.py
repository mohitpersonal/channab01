from django import template
register = template.Library()

@register.filter
def get_req(value):
	return value.title()


