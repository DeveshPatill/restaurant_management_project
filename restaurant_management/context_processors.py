from .models import Cart

def cart_item_count(request):
    if request.user.is_authentocated:
        return {"cart_item_count":Cart.objects.filter(user=request.user).count()}
    return {"cart_item_count": 0}


def breadcrumb_context(request):
    return{"breadcrumbs": getattr(request, "breadcrumbs",[])}

def current_time(request):
    return {
    'current_year': datetime.datetime.now().now
}