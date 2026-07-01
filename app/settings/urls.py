from django.urls import path

from app.settings.views import CategoryAPIView, ProductListAPIView, ProductCreateAPIView, ProductReadAPIView, ProductUpdateAPIView, ProductDeleteAPIView

urlpatterns = [
    path("category-list", CategoryAPIView.as_view(), name="category-list"),
    path("product-list", ProductListAPIView.as_view(), name="product-list"),
    path("product-create", ProductCreateAPIView.as_view(), name="create"),
    path("product-read", ProductReadAPIView.as_view(), name="read"),
    path("product-update", ProductUpdateAPIView.as_view(), name="update"),
    path("product-delete", ProductDeleteAPIView.as_view(), name="delete"),
]
