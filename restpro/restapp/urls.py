from django.urls import path
from django.views.generic import TemplateView

from .import views

urlpatterns = [
    path('register/' ,views.registerPage,name = 'register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_task>/', views.customer, name='customer'),
    path("demo/", TemplateView.as_view(template_name="accounts/main.html"), name="demo"),# sample

    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

]