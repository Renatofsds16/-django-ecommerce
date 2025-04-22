from . import views
from django.urls import path

urlpatterns = [
    path('',views.CreateView.as_view(),name='create'),
    path('update/',views.UpdateView.as_view(),name='update'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),

]
