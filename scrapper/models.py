from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    seller = models.CharField(max_length=255)
    rating = models.FloatField(null=True, blank=True)
    image_url = models.URLField()
    product_url = models.URLField()

    def __str__(self):
        return self.name    
    

class Articulo(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.URLField()
    precio = models.FloatField()
    url = models.URLField(max_length=2048)

    def __str__(self):
        return self.nombre
        