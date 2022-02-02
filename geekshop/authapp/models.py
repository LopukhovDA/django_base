from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(
        verbose_name="аватарка", upload_to="users_avatars", blank=True
    )
    age = models.PositiveIntegerField(verbose_name="возраст")
