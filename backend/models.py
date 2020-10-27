from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class Store(models.Model):
  name = models.CharField(max_length = 30)
  master = models.ForeignKey(User, on_delete = models.CASCADE)

  def __str__(self):
    return self.name + " Store"

  class Meta:
    verbose_name_plural='店铺'
    
class Commodity(models.Model):
  name = models.CharField(max_length = 30)
  char = models.CharField(max_length = 1)

  def __str__(self):
    return self.name + " " + self.char

  class Meta:
    verbose_name_plural='商品'

class Order(models.Model):
  name = models.CharField(max_length = 30)
  user_id = models.ForeignKey(User, on_delete = models.CASCADE)

  def __str__(self):
    return "{0}".format(self.id)

  class Meta:
    verbose_name_plural='订单'

class OrderCommodity(models.Model):
  commodity_id = models.ForeignKey(Commodity, on_delete = models.CASCADE)
  order_id = models.ForeignKey(Order, on_delete = models.CASCADE)
  count = models.IntegerField()