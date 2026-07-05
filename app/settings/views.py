from rest_framework.generics import ListAPIView, CreateAPIView,\
RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from app.settings.models import Category, Product
from app.settings.serializers import CategorySerializers, ProductSerializer

@method_decorator(cache_page(60*8, name="dispatch"))
class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def perform_create(self, serializer):
        serializer.save()
        cache.clear() 

class CategoryReadAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def perform_create(self, serializer):
        serializer.save()
        cache.clear()

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def perform_create(self, serializer):
        serializer.save()
        cache.clear()

@method_decorator(cache_page(60*5), name="dispatch")
class ProductListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ProductCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def perform_create(self, serializer):
        serializer.save()
        cache.clear() 

class ProductReadAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def perform_create(self, serializer):
        serializer.save()
        cache.clear()

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def perform_create(self, serializer):
        serializer.save()
        cache.clear()