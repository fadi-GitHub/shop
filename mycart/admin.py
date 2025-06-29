from django.contrib import admin
from django.utils.html import format_html
from .models import Product, PurchaseHistory, PurchaseItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_kg', 'quantity_in_stock', 'image_thumbnail')
    list_editable = ('price_per_kg', 'quantity_in_stock')

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "No Image"
    image_thumbnail.short_description = 'Image'


class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 0
    readonly_fields = ('product', 'quantity')


@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 'get_products_summary')
    list_filter = ('purchase_date',)
    inlines = [PurchaseItemInline]

    def get_products_summary(self, obj):
        items = obj.purchaseitem_set.all()
        return ", ".join([f"{item.quantity}kg of {item.product.name}" for item in items])
    get_products_summary.short_description = "Products Purchased"


@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('purchase_history', 'product', 'quantity')
    list_filter = ('purchase_history__purchase_date', 'product')
    search_fields = ('product__name',)