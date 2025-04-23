from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,View
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from . models import Variation
from pprint import pprint

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
        stock = variation.stock
        product = variation.product
        if variation.stock < 1:
            messages.error(self.request,'estoque insuficiente')
            return redirect(http_referer)
    
        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()
        cart = self.request.session['cart']
        product_id = product.pk
        product_name = product.name
        variation_name = variation.name or ''
        variation_id = variation.id
        price_unit = variation.price
        price_unit_promotional = variation.price_promotional
        price_product = variation.price
        quantity = 1 
        slug = product.slug
        image = product.image

        if image:
            image = image.url
        else:
            image = ''

        if vid in cart:
            quantity_cart = cart[vid]['quantity']
            quantity_cart += 1
            if stock < quantity_cart:
                messages.warning(
                    self.request,
                    'nao tem estoque suficiente'
                )
                quantity_cart = stock
        
            cart[vid]['quantity'] = quantity_cart
            cart[vid]['price_unit'] = price_unit * quantity_cart
            cart[vid]['price_unit_promotional'] = price_unit_promotional * quantity_cart
            cart[vid]['price_product'] = price_product

            



        ## {'cart':{}}
        else:
            cart[vid] = {
                'product_id':product_id,
                'product_name' : product_name,
                'variation_name' : variation_name,
                'variation_id' :variation_id,
                'price_unit' : price_unit,
                'price_unit_promotional':price_unit_promotional,
                'price_product':price_product,
                'quantity' : quantity,
                'slug' :slug,
                'image' :image
            }
        self.request.session.save()
        messages.success(self.request,'produdo adicionado com sucesso')
        return redirect('cart')
        

class RemoveCartView(View):
    def get(self,*args, **kwargs):
        http_referer = self.request.GET.get('HTTP_REFERER')
        vid = self.request.GET.get('vid')
        if not vid:
            return redirect('cart')
        if not self.request.session.get('cart'):
            return redirect('products')
        if not vid in self.request.session.get('cart'):
            messages.warning(self.request,'nao foi possivel apaga o item do carrinho')
            return redirect('products')
        cart = self.request.session.get('cart')
        messages.success(self.request,'o item foi apagado com sucesso')
        del self.request.session['cart'][vid]
        self.request.session.save()

        return redirect('cart')


class CartView(View):
    def get(self,*args, **kwargs):
        context = {'cart':self.request.session.get('cart')}
        return render(self.request,'produto/cart.html',context=context)


class FinishView(View):
    def get(self,*args, **kwargs):
        return HttpResponse('FinishView')
    
