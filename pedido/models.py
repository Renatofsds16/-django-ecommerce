from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    total = models.FloatField(default=0)
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
        )
    
    def __str__(self):
        return f'Pedido N. {self.pk}'
     

class ItemOrder(models.Model):
    class Meta:
        verbose_name = 'ItemOrder'
        verbose_name_plural = 'ItemOrders'
    order = models.ForeignKey(Order,models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation_id = models.PositiveIntegerField()
    price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.order}'
