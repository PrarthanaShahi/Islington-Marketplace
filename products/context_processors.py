from category.models import Category

def menu_links(request):
    """
    Context processor to make all Category objects available
    to all templates using the 'links' variable name.
    """
    links = Category.objects.all()
    return {'links': links}
