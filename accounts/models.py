from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    full_name = models.CharField('ФИО', max_length=200)
    phone = models.CharField(
        'Контактный телефон',
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?[\d\s\-\(\)]{10,20}$',
                message='Введите корректный номер телефона.',
            )
        ],
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
