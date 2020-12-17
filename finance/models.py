from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Category(models.Model):
    """Категории"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category", null=True)
    name = models.CharField("Название категория", max_length=150)
    count_amounts = 0

    def plus_amounts(self, count):
        self.count_amounts += count

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
