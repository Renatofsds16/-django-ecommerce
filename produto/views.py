from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,View
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from . models import Variation

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'produto/product_list.html'
    context_object_name = 'products'
    paginate_by = 20


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'produto/detail.html'
    slug_field = 'slug'


class AddCartView(View):
    def get(self,request):
        http_referer = self.request.GET.get('HTTP_REFERER')
        vid = self.request.GET.get('vid')
        if not vid:
            messages.error(self.request,'produto nao existe')
            return redirect(http_referer)
            
        variation = get_object_or_404(Variation,id=vid)
        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()
        cart = self.request.session['cart']
        if vid in cart:
            #TODO: variacao existe no carrinho
            ...
        else:
            #TODO: nao existe no carrinho
            ... 

        return HttpResponse(f'{variation}')
        

class RemoveCartView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('RemoveCartView')


class CartView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('CartViewView')


class FinishView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('FinishView')
    
