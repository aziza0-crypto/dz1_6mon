
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = 'CLIENT', 'Клиент'
        ADMIN = 'ADMIN', 'Администратор'

    bio = models.TextField(
        blank=True,
        verbose_name='О себе'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name='Подтверждён'
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT,
        verbose_name='Роль'
    )

    def __str__(self):
        return self.username
