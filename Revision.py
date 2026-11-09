"""
## Function-Based Views

@api_view(["GET", "POST"])
def product_list(request):
    # Get All Products
    if request.method == "GET":
        queryset = (
            Product.objects.select_related("collection").order_by("-id").all()[:5]
        )
        serializer = ProductSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    # Create A New Product
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)

    # Get a Product by ID
    if request.method == "GET":
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data)

    # Update a Product by ID
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete a Product by ID
    elif request.method == "DELETE":
        if product.order_items.count() > 0:  # type: ignore
            return Response(
                {
                    "error": "Product cannot be deleted because it is associated with an order item."
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
## ---------------------------------------------------------------
## Class-Based Views

 # Get All Products
    def get(self, request):
        queryset = (
            Product.objects.select_related("collection").order_by("-id").all()[:5]
        )
        serializer = ProductSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    # Create A New Product
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get a Product by ID
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data)

    # Update a Product by ID
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete a Product by ID
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.order_items.count() > 0:  # type: ignore
            return Response(
                {
                    "error": "Product cannot be deleted because it is associated with an order item."
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    # To Add More Logic To QuerySet
    def get_queryset(self):
        return Product.objects.select_related("collection").order_by("-id").all()[:5]

    # To Add More Logic To Serializer-Class
    def get_serializer_class(self):
        return ProductSerializer

# class ProductList(ListCreateAPIView):
#     pass
# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     pass
"""

"""
##  Function-Based Views

@api_view(["GET", "POST"])
def collection_list(request):
    # Get all collections and return them as a JSON response
    if request.method == "GET":
        queryset = Collection.objects.prefetch_related("products").all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new collection with the provided data and return it as a JSON response
    elif request.method == "POST":
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def collection_details(request, pk):
    # Get the collection object or return a 404 error if not found
    collection = get_object_or_404(Collection, pk=pk)
    if request.method == "GET":
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update the collection object with the provided data
    elif request.method == "PUT":
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete the collection object if it has no associated products
    elif request.method == "DELETE":
        if collection.products.count() > 0:  # type: ignore
            return Response(
                {
                    "error": "Collection cannot be deleted because it includes one or more products."
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class CollectionList(ListCreateAPIView):
#     pass
# class CollectionDetails(RetrieveUpdateDestroyAPIView):
#     pass
"""
