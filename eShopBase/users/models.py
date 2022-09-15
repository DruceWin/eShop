from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(verbose_name="Имя пользователя", unique=True, blank=True, null=True, max_length=30)
    phone = models.CharField(verbose_name="Номер телефона", unique=True, blank=True, null=True, max_length=13)
    email = models.EmailField(verbose_name="Email", unique=True)
    birthday = models.DateField(verbose_name="День рождения", blank=True, null=True,)
    address = models.CharField(verbose_name="Адрес", blank=True, null=True, max_length=200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        pass

