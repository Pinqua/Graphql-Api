from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

        
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=500)
    category=models.ForeignKey(to=Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

