from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.db.models import Q, F, Value, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Min, Max
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError

from store.models import Product, Collection, Order, OrderItem
from tags.models import TaggedItem

"""
## Testing the db connection

# from django.db import connection
# print(
#     connection.settings_dict["NAME"],
#     connection.settings_dict["HOST"],
#     connection.settings_dict["PORT"],
# )

# print(Product._meta.db_table)
# print(Product.objects.count())
# print(Product.objects.all().query)  # the SQL Django runs

## ---------------------------------------------------------
# query_set = (
#     OrderItem.objects.values(
#         "product__id",
#         "product__title",
#         "product__unit_price",
#         "product__collection__title",
#     )
#     .distinct()
#     .order_by("product__title")
# )

# query_set = Product.objects.filter(
#     id__in=OrderItem.objects.values(
#         "product_id",
#     ).distinct()
# ).order_by("title")

# query_set = (
#     Order.objects.select_related("customer")
#     .prefetch_related("orderitem_set__product")
#     .order_by("-placed_at")[:5]
# )

# result = Product.objects.aggregate(
#     total_products=Count("id"),
#     min_price=Min("unit_price"),
#     max_price=Max("unit_price"),
#     avg_price=Avg("unit_price"),
#     total_inventory=Sum("inventory"),
# )

# queryset = Product.objects.annotate(
#   discounted_price=ExpressionWrapper(
#         F("unit_price") * 0.8,
#         output_field=DecimalField(max_digits=10, decimal_places=2),
#     )
# ).order_by("title")[:5]

## --------------- 
## CRUD Operations
### Create New Object
# collection = Collection()
# collection.title = "Video Games"
# collection.featured_product = Product(pk=1)
# collection.save()
# print(collection.id) # type: ignore

## Updating An Object
# collection = Collection.objects.get(pk=11)
# collection.featured_product = Product(pk=2)
# collection.save()
# print(collection.id) # type: ignore
# OR:
# Collection.objects.filter(pk=11).update(featured_product=None)

## Deleting An Object
# collection = Collection(pk=11)
# collection.delete()
# OR:
# Collection.objects.filter(pk=11).delete()
    
## ------------
## Transactions
# with transaction.atomic():
#     order = Order()
#     order.customer_id = 1  # type: ignore
#     order.save()

#     item = OrderItem()
#     item.order = order
#     item.product_id = -1  # type: ignore
#     item.quantity = 1
#     item.unit_price = 10
#     item.save()

## ---------------
## Writing Raw SQL
# with connection.cursor() as cursor:
#     cursor.execute("SELECT * FROM store_product")
#     cursor.close()
"""


def index(request):
    return HttpResponse("Hello From Playground Application !!")


def say_hello(request):

    return render(
        request,
        "hello.html",
        {"name": "", "results": list()},
    )
