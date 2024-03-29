from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField
    description = models.TextField
    count = models.IntegerField
    def to_json(self):
        return {
            'id' : self.id,
            'price' : self.price,
            'description' : self.description,
            'count' : self.count
        }
class Category(models.Model):
    name = models.CharField(max_length=300)