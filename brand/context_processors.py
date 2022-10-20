from .models import brand 


def menu_links_brand(request):
    link=brand.objects.all()
    return dict(link=link)
