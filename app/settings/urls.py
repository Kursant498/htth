from django.urls import path

from app.settings.views import (
      CategoryAPIView, ProductListAPIView, ProductCreateAPIView,
      ProductReadAPIView, ProductUpdateAPIView, ProductDeleteAPIView,
      CategoryCreateAPIView, CategoryReadAPIView, CategoryUpdateAPIView,
      CategoryDeleteAPIView)

urlpatterns = [
    path("category-list", CategoryAPIView.as_view(), name="category-list"),
    path("product-list", ProductListAPIView.as_view(), name="product-list"),
    path("product-create", ProductCreateAPIView.as_view(), name="create"),
    path("product-read/<int:pk>/", ProductReadAPIView.as_view(), name="read"),
    path("product-update/<int:pk>/", ProductUpdateAPIView.as_view(), name="update"),
    path("product-delete/<int:pk>/", ProductDeleteAPIView.as_view(), name="delete"),
    path("category-create", CategoryCreateAPIView.as_view(), name="c_create"),
    path("category-read/<int:pk>/", CategoryReadAPIView.as_view(), name="c_read"),
    path("categoru-update/<int:pk>/", CategoryUpdateAPIView.as_view(), name="c_update"),
    path("category-delete", CategoryDeleteAPIView.as_view(), name="c_delete"),
]