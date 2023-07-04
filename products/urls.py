from django.urls import path
from products.views import ListCreateManufacturersView, ListCreateCategoriesView, ListCreateProductsView

urlpatterns = [
    path("manufacturers/", ListCreateManufacturersView.as_view(), name="manufacturers-list-create"),
    path("categories/", ListCreateCategoriesView.as_view(), name="categories-list-create"),
    path("products/", ListCreateProductsView.as_view(), name="products-list-view"),
]
