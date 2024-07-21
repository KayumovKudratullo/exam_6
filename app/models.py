from django.db import models
from User.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Cook(models.Model):
    full_name = models.CharField(max_length=150)
    img = models.ImageField()


    class Meta():
        verbose_name = 'Cook'
        verbose_name_plural = 'Cooks'

    def __str__(self) -> str:
        return self.full_name


class Banner(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField()


    class Meta():
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self) -> str:
        return self.title


class Meal(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    class Meta():
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

    def __str__(self) -> str:
        return self.name


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField()

    class Meta():
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUS'

    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta():
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return f"{self.author.username}"
    

class Reserve(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    date = models.DateField()
    party  = models.CharField(max_length=20)

    class Meta():
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.full_name