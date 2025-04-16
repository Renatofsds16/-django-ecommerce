from django.contrib import admin
from . models import UserProfile,Adress

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = 'user','age','date_of_birth','cpf','adress',
    list_display_links = 'user','cpf','adress',




@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    list_display = 'rua','number','complement','bairro','cep','city','state',
    list_display_links = 'rua','number','bairro',
