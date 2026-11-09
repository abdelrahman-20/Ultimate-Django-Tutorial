from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()  # type: ignore
router.register("collections", views.CollectionViewSet)
router.register("products", views.ProductViewSet, basename="products")
router.register("carts", views.CartsViewSet, basename="carts")

products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

# URLConf
urlpatterns = router.urls + products_router.urls

"""
# from rest_framework.routers import DefaultRouter
# from django.urls import include, path
# from pprint import pprint
# pprint(router.urls)
# path("products/", views.ProductList.as_view()),
# path("products/<int:pk>/", views.ProductDetails.as_view()),
# path("collections/", views.CollectionList.as_view()),
# path(
#     "collections/<int:pk>/",
#     views.CollectionDetails.as_view(),
#     name="collection-details",
# ),
"""
