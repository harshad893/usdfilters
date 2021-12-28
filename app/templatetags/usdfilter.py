from django import template
register=template.Library()
def swap(value):
    return value.swapcase()

@register.filter()
def replace_char(value,arg):
    return value.replace(arg,'b')



register.filter('swapping',swap)
#register.filter('rep',replace_char)