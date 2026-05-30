from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    seller = models.CharField(max_length=100)
    rating = models.FloatField(default=5)
    image = models.ImageField(upload_to='products/')
    top = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class WeddingCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WeddingProduct(models.Model):
    category = models.ForeignKey(WeddingCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    seller = models.CharField(max_length=100)
    rating = models.FloatField(default=5)
    image = models.ImageField(upload_to='products/')
    top = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    