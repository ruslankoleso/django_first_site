from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    materials = models.TextField()
    articul = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.name