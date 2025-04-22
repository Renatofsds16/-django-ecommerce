from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.[]
class PayView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('pagar')

class CloseOrderView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('fechar pedido')

class DetailView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('detalhes pedido')
    