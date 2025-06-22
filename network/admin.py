from django.contrib import admin
from django.utils.html import format_html
from .models import Network, Product


class ProductInline(admin.TabularInline):
    model = Network.products.through
    extra = 1


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'supplier_link', 'city', 'debt', 'creation_time')
    list_filter = ('city', 'level')
    exclude = ('products',)
    inlines = [ProductInline]
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html(
                '<a href="/admin/network/network/{}/change/">{}</a>',
                obj.supplier.id,
                obj.supplier
            )
        return "-"
    supplier_link.short_description = 'Supplier'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
    clear_debt.short_description = "Clear debt for selected networks"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')