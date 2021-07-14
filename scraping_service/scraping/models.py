from django.db import models
from django.db.models import CharField
from .utils import from_cyrillic_to_eng


def default_urls():
    return {"superjob": "", "careerist": "", "jooble": ""}

class City(models.Model):
    name = CharField(max_length=50, verbose_name='Название населенного пункта', unique=True)
    slug = CharField(max_length=50, blank=True, unique=True)
    
    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Названия населенных пунктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)



class Language(models.Model):
    name = CharField(max_length=50, verbose_name='Язык программирования', unique=True)
    slug = CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)



class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = CharField(max_length=250, verbose_name='Заголовок вакансии')
    company = CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык программирования')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


class Error(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()



class Url(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык программирования')
    url_data = models.JSONField(default=default_urls)

    class Meta:
        unique_together = ("city", "language")
