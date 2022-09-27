from django.db import models

# Create your models here.
class Clothes(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to = 'images/')
    price = models.DecimalField(decimal_places=2, max_digits=20)
    description = models.TextField()
    

    def __str__(self):
        return self.name