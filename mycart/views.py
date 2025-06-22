from django.shortcuts import render
from django.contrib import messages
from .forms import CartForm
from .models import Product

def cart_view(request):
    products = Product.objects.all()
    form = CartForm(request.POST or None, products=products)

    if request.method == 'POST' and form.is_valid():
        cart_items = []
        for product in products:
            field_name = f"product_{product.id}"
            requested_qty = form.cleaned_data.get(field_name, 0)

            if requested_qty and requested_qty > 0:
                if not product.is_available(requested_qty):
                    messages.error(request, product.get_stock_message(requested_qty))
                else:
                    cart_items.append((product, requested_qty))
            else:
                messages.error(request, f"Invalid quantity for {product.name}. Please enter a valid number.")

        if not messages.get_messages(request):
            for product, requested_qty in cart_items:
                product.reduce_stock(requested_qty)
            messages.success(request, "Order confirmed successfully!")
            form = CartForm(products=products)

    return render(request, 'mycart/mycart.html', {
        'form': form,
        'products': products,
    })
