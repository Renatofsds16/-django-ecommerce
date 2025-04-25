from django.forms import ModelForm,ValidationError
from django.contrib.auth.models import User
from . import models 
from django.forms import CharField,PasswordInput



class PerfilForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        exclude = ('user',)

class UserForm(ModelForm):
    password = CharField(max_length=255, required=False,widget=PasswordInput(),label='senha')
    password2 = CharField(max_length=255, required=False,widget=PasswordInput(),label='repita a senha')
    def __init__(self,user=None,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password','email',)
    
    
    def clean(self):
        cleaned_data = self.cleaned_data
        validation_error_messages = {}
        email = cleaned_data['email']
        first_name = cleaned_data['first_name']
        last_name = cleaned_data['last_name']
        user_db = cleaned_data['username']
        password = cleaned_data['password']
        password2 = cleaned_data['password2']
        email_db = User.objects.filter(email=email).first()
        if len(first_name) < 3:
            validation_error_messages['first_name'] = 'primeiro nome muito curto'
        if len(last_name) < 3:
            validation_error_messages['last_name'] = 'sobrenome muito curto'
        
        if email_db:
            validation_error_messages['email'] = 'email ja existe'
        if not email:
            validation_error_messages['email'] = 'email invalido'
        

        if len(last_name) < 3:
            validation_error_messages['last_name'] = 'sobrenome muito curto'
        if not user_db or len(user_db) < 6:
            validation_error_messages['username'] = 'digite o seu username'
        
        if len(password)< 6:
            validation_error_messages['password'] = 'senha e muito curta'
        
        if password:
            if password != password2:
                validation_error_messages['password'] = 'as senhas nao sao iguais'
                validation_error_messages['password2'] = 'as senhas nao sao iguais'
        
        if validation_error_messages:
            raise(ValidationError(validation_error_messages))
        

        
        

        if self.user:
            ...
            

        else:
            validation_error_messages['username'] = 'bla bla bla bla'

         
        if self.user:
            print('logado')
            print('logado')
            print('logado')
            print('logado')
            print(cleaned_data['username'])
        
        else:
            print('usuario nao logago')

        return super().clean()

