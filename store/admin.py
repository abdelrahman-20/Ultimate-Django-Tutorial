from collections.abc import Iterable
from typing import Any

from django.contrib import admin
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from store.models import Collection, Customer, Order, Product


class InventoryFilter(admin.SimpleListFilter):
    title = "Inventory"
    parameter_name = "inventory"

    def lookups(self, request: HttpRequest, model_admin: admin.ModelAdmin):
        return [("<10", "Low")]

    def queryset(
        self, request: HttpRequest, queryset: QuerySet[Any, Any]
    ) -> QuerySet[Any, Any] | None:
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_per_page = 50
    list_select_related = ["collection"]
    list_filter = ["collection", InventoryFilter]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "LOW"
        return "OK"

    @admin.action(description="Clear Inventory")
    def clear_inventory(self, request: HttpRequest, queryset: QuerySet):
        pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "membership"]
    list_editable = ["email", "membership"]
    ordering = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "product_count"]

    @admin.display(ordering="product_count")
    def product_count(self, collection):
        # Building The URL+Query For Each Collection Products:
        # reverse("admin:app_model_page")
        url = (
            reverse("admin:store_product_changelist")
            + "?"
            + urlencode({"collection__id": str(collection.id)})
        )

        return format_html("<a href='{}'>{}</a>", url, collection.product_count)
        # return collection.product_count

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).annotate(product_count=Count("products"))

    class Meta:
        ordering = "title"



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ["customer"]
    list_display = ["id", "placed_at", "payment_status", "customer"]
    list_select_related = ["customer"]
    ordering = ["id"]
