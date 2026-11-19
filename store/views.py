from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .filters import ProductFilter
from .models import Cart, Collection, Customer, OrderItem, Product, Review
from .pagination import DefaultPagination
from .serializers import (
    CartSerializer,
    CollectionSerializer,
    CustomerSerializer,
    ProductSerializer,
    ReviewSerializer,
)

"""Revision"""


class ProductList(ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.select_related("collection").order_by("-id").all()

    def get_serializer_class(self):
        return ProductSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class ProductDetails(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Product.objects.select_related("collection").order_by("-id").all()

    def get_serializer_class(self):
        return ProductSerializer

    def destroy(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs["pk"])
        if product.order_items.count() > 0:  # type: ignore
            return Response(
                {
                    "error": "Product cannot be deleted because it is associated with an order item."
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )


class CollectionList(ListCreateAPIView):

    def get_queryset(self):
        return Collection.objects.annotate(products_count=Count("products")).all()

    def get_serializer_class(self):
        return CollectionSerializer


class CollectionDetails(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Collection.objects.annotate(products_count=Count("products")).all()

    def get_serializer_class(self):
        return CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        collection = get_object_or_404(Collection, pk=kwargs["pk"])

        if collection.products.count() > 0:  # type: ignore
            return Response(
                {
                    "error": "Collection cannot be deleted because it includes one or more products.!!!"
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def delete(self, request, pk):
    #     collection = get_object_or_404(Collection, pk=pk)
    #     if collection.products.count() > 0:  # type: ignore
    #         return Response(
    #             {
    #                 "error": "Collection cannot be deleted because it includes one or more products.!!!"
    #             },
    #             status=status.HTTP_405_METHOD_NOT_ALLOWED,
    #         )

    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


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


"""Customer ViewSet"""


class CustomersViewSet(
    CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # @action(detail=False)
    # def me(self, request):
    #     customer = Customer.objects.get(pk=request.user.id)
    #     serializer = CustomerSerializer(customer)
    #     return Response(request.user)
