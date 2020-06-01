from django.db import models

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_size = models.CharField(max_length=3, default="")
    item_cost = models.FloatField()