from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Category(models.Model):
    """Категории"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category", null=True)
    name = models.CharField("Название категория", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Label(models.Model):
    """Лейблы"""
    name = models.CharField("Лейблы", max_length=150)
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Лейбл"
        verbose_name_plural = "Лейблы"


class Amount(models.Model):
    """Расходы"""
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)
    label = models.ForeignKey(Label, verbose_name="Лейблы", on_delete=models.CASCADE)
    amount = models.IntegerField("Расходы")
    add_date = models.DateField("Дата добавления расхода", default=date.today)

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name = "Количество"
        verbose_name_plural = "Количество"

