from pages.models import Page

def get_page(request):
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')

    return {
        'pages': pages
    }