from django.db import models
from django.conf import settings
from mainapp.models import Product
from django.utils.functional import cached_property


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(
        verbose_name="время", auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk:
            basket_item = Basket.objects.filter(pk=self.pk)
            self.product.quantity -= self.quantity - \
                basket_item[0].quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)

    @cached_property
    def get_items_cached(self):
        return Basket.objects.filter(user=self.user).select_related()

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = self.get_items_cached
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    @property
    def total_cost(self):
        _items = self.get_items_cached
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost
