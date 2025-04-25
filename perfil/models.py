from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils.validacpf import valida_cpf
import re

# Create your models here.

class Adress(models.Model):
    class Meta:
        verbose_name = 'Adress'
        verbose_name_plural = 'Adreses'
    rua = models.CharField(max_length=255)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    state = models.CharField(
        default='PB',
        max_length=2,
        choices=(
                ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
        )
    
    def __str__(self):
        return f'{self.rua} {self.number}'
    
    def clean(self):
        error_messages = {}
        if re.search(r'[^0-9]',self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'Cep inválido'
        if error_messages:
            raise ValidationError(message=error_messages)
        return super().clean()

class UserProfile(models.Model):
    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField(verbose_name='idade')
    date_of_birth = models.DateField(verbose_name='data de nascimento')
    cpf = models.CharField(max_length=15,verbose_name='cpf')
    adress = models.ForeignKey(Adress,on_delete=models.SET_NULL,null=True,verbose_name='Endereço')

    def __str__(self):
        return f'{self.user.first_name}'
    

    def clean(self):
        error_messages = {}
        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um cpf válido'
        if error_messages:
            raise ValidationError(message=error_messages)
        return super().clean()