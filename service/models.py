from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='услуга')
    price = models.IntegerField(**NULLABLE, verbose_name='цена')
    desc = models.TextField(**NULLABLE, verbose_name='описание')
    contraindications = models.TextField(**NULLABLE, verbose_name='противопоказания')
    img = models.ImageField(**NULLABLE, verbose_name='изображение')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
