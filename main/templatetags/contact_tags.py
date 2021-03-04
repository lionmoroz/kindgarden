from django import template
from ..models import ContactInfo
register = template.Library()


@register.inclusion_tag('include/contact_info_navbar.html')
def contact_nav():
    contact_info = ContactInfo.objects.all()  
    return {'contact_info': contact_info}