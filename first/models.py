from django.db import models

# Create your models here.


class StockItem(models.Model):
    date=models.TextField()
    trans = models.TextField()
    symbol = models.TextField()
    qty = models.IntegerField()
    price = models.IntegerField()

