from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    picture_url = models.CharField(max_length=512)
    description = models.TextField()
    product_name = models.CharField(max_length=128)

class Buyer(models.Model):
    owner = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    description = models.TextField()

class Action(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user_id = models.CharField(max_length=32)
    context_product = models.CharField(max_length=128)
    no_of_actions = models.IntegerField()

