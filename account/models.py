from django.conf import settings
from django.db import models


class Profile(models.Model):
    """ Модель профиля пользователя"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    photo = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return f'Profile of {self.user.username}'
