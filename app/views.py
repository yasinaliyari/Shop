from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from app.models import Order, OrderItem


@require_GET
def checkout(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    items = OrderItem.objects.filter(order=order).select_related("product")
    total_price = sum(item.product.price * item.quantity for item in items)
    return JsonResponse({"total_price": format(total_price, ".6f")})
