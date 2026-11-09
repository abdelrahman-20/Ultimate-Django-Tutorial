from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .filters import ProductFilter
from .models import Cart, Collection, OrderItem, Product, Review
from .pagination import DefaultPagination
from .serializers import (
    CartSerializer,
    CollectionSerializer,
    ProductSerializer,
    ReviewSerializer,
)

"""Collections Controllers"""


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.prefetch_related("products").all().order_by("-id")
    serializer_class = CollectionSerializer

    # Override The "Destroy" Function For The "RetrieveUpdateDestroyAPIView" Class
    def destroy(self, request, pk):
        # (*args, **kwargs), if Product.objects.filter(collection_id=kwargs["pk"]).count() > 0:
        # else: return super().destroy(request, *args, **kwargs)
        collection = get_object_or_404(Collection, pk=pk)

        if collection.products.count() > 0:  # type: ignore
            return Response(
                {
                    "error": "Collection cannot be deleted because it includes one or more products.!!!"
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        else:
            collection.delete()
            return Response(
                {"message": f"Collection with ID: {pk} was deleted Successfully !!"},
                status=status.HTTP_204_NO_CONTENT,
            )


"""Products Controllers"""


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer

    # Generic Filtering, Searching, And Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_class = ProductFilter  # Custom Filtering Class (filterset_fields)
    search_fields = ["title", "description"]
    ordering_fields = ["unit_price", "title"]

    # Pagination
    pagination_class = DefaultPagination

    # Override The Context Object
    def get_serializer_context(self):
        return {"context": self.request}

    # Override The "Destroy" Function For The "RetrieveUpdateDestroyAPIView" Class
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count() > 0:
            return Response(
                {
                    "error": "Product cannot be deleted because it is associated with an order item."
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        else:
            return super().destroy(request, *args, **kwargs)


"""Reviews Controllers"""


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs["product_pk"])

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}


"""Carts Controllers"""


class CartsViewSet(
    CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet
):
    queryset = Cart.objects.prefetch_related("items__product")
    serializer_class = CartSerializer
