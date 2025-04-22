from django.db import models
from PIL import Image
from django.conf import settings
from pathlib import Path
from utils.resize_image import resize_image
from django.utils.text import slugify
from utils.real import format_price_real

# Create your models here.
class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    description_long = models.TextField()
    image = models.ImageField(
        upload_to='produto_images/%Y/%m',blank=True,null=True
    )
    slug = models.SlugField(unique=True,blank=True,null=True)
    price_marketing = models.FloatField(default=0)
    price_marketing_promotional = models.FloatField(default=0)
    type = models.CharField(default='V',max_length=1,choices=(('V','Variavel'),('S','Simples')))

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}'
            self.slug = slug
        super().save(*args,**kwargs)
        if self.image:
            resize_image(img=self.image,new_width=800)
    
    
    

class Variation(models.Model):
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    price = models.FloatField(default=0)
    price_promotional = models.FloatField(default=0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
