from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='post/', **NULLABLE, verbose_name='Изображение')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    publication_sign = models.BooleanField(default=True, verbose_name='Признак публикации')
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'