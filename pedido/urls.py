from . import views
from django.urls import path


urlpatterns = [
    path('',views.PayView.as_view(),name='pay'),
    path('closeorder/',views.CloseOrderView.as_view(),name='close_order'),
    path('detail/',views.DetailView.as_view(),name='detail'),
]