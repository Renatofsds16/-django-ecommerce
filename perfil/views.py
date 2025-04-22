from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class CreateView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('CreateView')

class UpdateView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('UpdateView')


class LoginView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('LoginView')


class LogoutView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('LogoutView')

    