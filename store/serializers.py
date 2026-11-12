from decimal import Decimal
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from rest_framework import serializers
from store.models import Cart, CartItem, Customer, Product, Collection, Review

"""
Collection Serializer
"""


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "product_count", "collection_link"]

    product_count = serializers.SerializerMethodField(method_name="get_product_count")
    collection_link = serializers.SerializerMethodField(
        method_name="get_collection_link"
    )

    def get_product_count(self, collection: Collection):
        return collection.products.count()  # type: ignore

    def get_collection_link(self, collection: Collection):
        url = "http://127.0.0.1:8000/store/collections/" + str(collection.id)  # type: ignore

        return format_html("{}", url)  # type: ignore


"""
Products Serializer
"""


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "price",
            "price_with_tax",
            "inventory",
            "collection",
        ]

    price = serializers.DecimalField(6, 2, source="unit_price")
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.slug = "*".join(str(product.slug).split("-"))
    #     product.save()
    #     return product

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get("unit_price")
    #     instance.save()
    #     return instance

    """
    ## Hyper-Link
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name="collection-details",
    # )
    ## Nested Object
    # collection = CollectionSerializer()
    """


"""
Reviews Serializer
"""


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "name",
            "description",
            "date",
        ]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)


"""
Cart-Items Serializer
"""


# Get The Necessary Product Fields
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "unit_price"]


"""
Cart Items Serializer
"""


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(method_name="get_total_price")

    def get_total_price(self, cartItem: CartItem):
        return cartItem.quantity * cartItem.product.unit_price

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "total_price"]


"""
Cart Serializer
"""


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name="get_total_price")

    def get_total_price(self, cart: Cart):
        return sum([item.product.unit_price * item.quantity for item in cart.items.all()])  # type: ignore

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]


"""
Customer Serializer
"""


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "birth_date",
            "membership",
        ]
