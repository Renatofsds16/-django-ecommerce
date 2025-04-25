from . import views
from django.urls import path


urlpatterns = [
    path('',views.PayView.as_view(),name='pay'),
    path('saveoder/',views.SaveOrder.as_view(),name='saveoder'),
    path('detail/',views.DetailView.as_view(),name='detail'),
]