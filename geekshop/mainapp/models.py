from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=100, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="имя продукта", max_length=100)
    main_desc = models.CharField(
        verbose_name="краткое описание продукта", max_length=60, blank=True
    )
    description = models.TextField(verbose_name="описание продукта", blank=True)
    price = models.DecimalField(
        verbose_name="цена продукта", max_digits=8, decimal_places=2, default=0
    )
    image = models.ImageField(
        verbose_name="изображение продукта", upload_to="products_images", blank=True
    )
    quantity = models.PositiveIntegerField(
        verbose_name="количество товара на складе", default=0
    )
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
