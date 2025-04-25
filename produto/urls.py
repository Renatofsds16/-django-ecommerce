from . import views
from django.urls import path

urlpatterns = [
    path('',views.ProductListView.as_view(),name='products'),
    path('product/<slug:slug>/',views.ProductDetailView.as_view(),name='product'),
    path('addcart/id/',views.AddCartView.as_view(),name='addcart'),
    path('removecart/',views.RemoveCartView.as_view(),name='removecart'),
    path('cart/',views.CartView.as_view(),name='cart'),
    path('resume/',views.ResumeView.as_view(),name='resume'),
]