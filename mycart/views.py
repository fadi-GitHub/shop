from django.shortcuts import render
from django.contrib import messages
from django.db.models import Sum
from .forms import CartForm
from .models import Product, PurchaseHistory, PurchaseItem

def cart_view(request):
    products = Product.objects.all()
    form = CartForm(request.POST or None, products=products)
    cart_items = []
    has_error = False

    if request.method == 'POST' and form.is_valid():
        for product in products:
            field_name = f"product_{product.id}"
            requested_qty = form.cleaned_data.get(field_name, 0)
            if requested_qty and requested_qty > 0:
                if not product.is_available(requested_qty):
                    messages.error(request, product.get_stock_message(requested_qty))
                    has_error = True
                else:
                    cart_items.append((product, requested_qty))
            else:
                messages.error(request, f"Invalid quantity for {product.name}. Please enter a valid number.")
                has_error = True

        if cart_items and not has_error:
            purchase_history = PurchaseHistory.objects.create()
            for product, requested_qty in cart_items:
                product.reduce_stock(requested_qty)
                PurchaseItem.objects.create(
                    purchase_history=purchase_history,
                    product=product,
                    quantity=requested_qty,
                    total_price=product.price_per_kg * requested_qty,
                )
            purchase_history.save()
            messages.success(request, "Order confirmed successfully!")
            form = CartForm(products=products)

    return render(request, 'mycart/mycart.html', {
        'form': form,
        'products': products,
    })

def purchase_history_view(request):
    purchase_histories = PurchaseHistory.objects.all().order_by('-purchase_date').prefetch_related('purchaseitem_set__product')
    total = purchase_histories.aggregate(total=Sum('purchaseitem__total_price'))['total'] or 0
    return render(request, 'mycart/purchase_history.html', {
        'purchase_histories': purchase_histories,
        'total_price': total,
    })