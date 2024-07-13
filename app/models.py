from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Cook(models.Model):
    full_name = models.CharField(max_length=150)
    img = models.ImageField()

    def __str__(self) -> str:
        return self.full_name


class Banner(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField()

    def __str__(self) -> str:
        return self.title


class Meals(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField()

    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username}"
    

class Reserve(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    date = models.DateField()
    party  = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name