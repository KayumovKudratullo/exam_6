from django.db import models
from app.models import Cook, Category


class SpecialMeal(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    class Meta():
        verbose_name = 'Special_Meal'
        verbose_name_plural = 'Special_Meals'

    def __str__(self) -> str:
        return self.name