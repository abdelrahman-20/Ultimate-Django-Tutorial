from django.urls import include, path
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from . import views

# router = routers.DefaultRouter()  # type: ignore
# router.register("collections", views.CollectionViewSet)
# router.register("products", views.ProductViewSet, basename="products")
# router.register("carts", views.CartsViewSet, basename="carts")
# router.register("customers", views.CustomersViewSet)

# products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
# products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

# URLConf
# urlpatterns = router.urls + products_router.urls

router = DefaultRouter()

router.register("products", views.ProductViewSet_Revision, basename="product")
router.register("collections", views.CollectionViewSet_Revision, basename="collection")

urlpatterns = router.urls
