from django.db import models
from datetime import date


class Category(models.Model):
    """Категории"""
    name = models.CharField("Название категория", max_length=150)
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Label(models.Model):
    """Лейблы"""
    name = models.CharField("Лейблы", max_length=150)
    categories_id = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Лейбл"
        verbose_name_plural = "Лейблы"


class Amount(models.Model):
    """Расходы"""
    categories_id = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)
    labels_id = models.ForeignKey(Label, verbose_name="Лейблы", on_delete=models.CASCADE)
    amount = models.IntegerField("Расходы")
    date_add = models.DateField("Дата добавления расхода", default=date.today)

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name = "Количество"
        verbose_name_plural = "Количество"
