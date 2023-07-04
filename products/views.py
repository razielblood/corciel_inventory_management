from rest_framework.generics import ListCreateAPIView
from products.models import Manufacturer, Category, Product
from products.serializers import (
    ManufacturerSerializer,
    CategorySerializer,
    ProductCreateSerializer,
    ProductRetrieveSerializer,
)


# Create your views here.
class ListCreateManufacturersView(ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ListCreateCategoriesView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCreateProductsView(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductRetrieveSerializer
