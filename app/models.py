from django.db import models

# Create your models here.
class destination(models.Model):
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    offer = models.BooleanField(default=False)