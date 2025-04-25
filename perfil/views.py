from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from . forms import UserForm,PerfilForm

# Create your views here.
class BaseProfile(View):
    template_name = 'perfil/create.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        if self.request.user.is_authenticated:
            self.context = {
            'userform': UserForm(data=self.request.POST or None,user=self.request.user,instance=self.request.user),
            'perfilform': PerfilForm(data=self.request.POST or None)
            }
        else:
            self.context = {
            'userform': UserForm(data=self.request.POST or None),
            'perfilform': PerfilForm(data=self.request.POST or None)
            }
        self.renderizar = render(self.request,self.template_name,self.context)
    
    def get(self,*args, **kwargs):
        return self.renderizar
    


class CreateView(BaseProfile):
    def post(self,*args,**kwargs):
        return self.renderizar

class UpdateView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('UpdateView')


class LoginView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('LoginView')


class LogoutView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('LogoutView')

    