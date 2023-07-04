from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    slug = models.SlugField(max_length=64)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    slug = models.SlugField(max_length=64)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    pieces_per_package = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    image = models.ImageField(blank=True)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.PROTECT, related_name="products")
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name="products")

    def __str__(self) -> str:
        return_value = f"{self.name}"
        if self.weight_kg is not None:
            return_value += f"[{self.weight_kg} KG]"
        if self.pieces_per_package is not None:
            return_value += f"[{self.pieces_per_package} unidades]"
        return_value += f" - {self.manufacturer.name}"
        return return_value
