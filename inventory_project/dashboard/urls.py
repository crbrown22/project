from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name ='homepage'),
    path('about/', views.about, name ='about'),
    path('flexmob/', views.flexmob, name ='flexmob'),
    path('conditioning/', views.conditioning, name ='conditioning'),
    path('power/', views.power, name ='power'),
    path('members/', views.members, name ='members'),
    path('index/', views.index, name ='index'),
    path('index/staff/', views.staff, name ='staff'),
    path('index/staff/details/<int:pk>/', views.staff_details, name ='staff-details'),
    path('index/staff/delete/<int:pk>', views.staff_delete, name ='staff-delete'),
    path('index/products/', views.products, name ='products'),
    path('index/orders/', views.orders, name ='orders'),
    path('index/orders/orders_staff', views.orders_staff, name ='orders-staff'),
    path('index/products/delete/<int:pk>', views.product_delete, name ='product-delete'),
    path('index/products/edit/<int:pk>', views.product_update, name ='product-update')
]