import string
from random import choice

from django.db import models

from eShopBase.settings import ALLOWED_HOSTS


class ModelShortURL(models.Model):
    """
    Модель для длинных и коротких ссылок
    """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    long_URL = models.URLField(verbose_name="Длинный URL", max_length=200)
    short_URL = models.URLField(max_length=250, unique=True)

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        length = 6
        char = string.ascii_letters + string.digits
        short_id = "".join(choice(char) for _ in range(length))
        short = ALLOWED_HOSTS[0]
        self.short_URL = short + ':8000/' + short_id
        super(ModelShortURL, self).save(*args, **kwargs)
